"""
Rosalind problem mmch: http://rosalind.info/problems/mmch/

Author: Michael Ayars

Given:  A positive integer n (n≤1000).

Return:   The total number of subsets of {1,2,…,n} modulo 1,000,000.
"""


from itertools import chain, combinations


def count_subsets(n):
    return (2**n)%1000000

if __name__ == "__main__":

    print(count_subsets(880))
