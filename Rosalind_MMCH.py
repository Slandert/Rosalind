"""
Rosalind problem mmch: http://rosalind.info/problems/mmch/

Author: Michael Ayars

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s
"""

from math import factorial


def max_matchings(seq):
    """
    seq = RNA string

    Returns the total possible number of maximum matchings of basepair edges in the bonding graph of seq
    """

    a = seq.count("A")
    u = seq.count("U")
    g = seq.count("G")
    c = seq.count("C")

    max_au = max(a, u)
    min_au = min(a, u)
    max_gc = max(g, c)
    min_gc = min(g, c)

    fact_au = factorial(max_au) // factorial(max_au - min_au)
    fact_gc = factorial(max_gc) // factorial(max_gc - min_gc)

    return fact_au * fact_gc


if __name__ == "__main__":

    #input file contains a single FASTA sequence
    dataset = open('inputData/rosalind_input_mmch.txt').readlines()

    print(max_matchings(dataset[1].strip()))

