"""
Rosalind problem lcsq: http://rosalind.info/problems/lcsq/

Author: Michael Ayars

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)


Needed some help with this one.  Original approach was similar to SW, but a little off and couldn't handle the input length.
"""


from Bio import SeqIO
from numpy import zeros


def longest_common_substring(seq1, seq2):
    """
    seq1, seq2 : DNA strings 
    """
    result_ss = ''
    i = 0
    for i in range(len(seq1)+1):
        common_ss = remaining_substring(seq1[i:],seq2)
        if len(common_ss) > len(result_ss):        
            result_ss = common_ss
            print(" result = " + ' ' + result_ss)
    return result_ss


def LCSLength(seq1, seq2):
    """
    Smith-Waterman algorithm: https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm

    In brief, builds a table comparing from each start/break point how many continuous bases match in the resulting segments (and segments within those).
    Dynamically backtracking through this table returns the optimal sequence/gap pattern for longest common subsequence.

    seq1, seq2 : DNA strings
       
    """

    
    m = len(seq1)
    n = len(seq2)

    table = zeros((m+1, n+1))

    for i in range(m):
        for j in range(n):
            if seq1[i] == seq2[j]:
                table[i+1, j+1] = table[i,j] + 1
                print(table)
            else:
                table[i+1,j+1] = max(table[i+1,j], table[i,j+1])
                print(table)
    return table


def remaining_substring(seq1, seq2):
    if len(seq1) > 0 and len(seq2) > 0:
        for i in range(len(seq1) + 1):
            print(i)
            first_index = seq2.find(seq1[i])
            if first_index > -1:
                return seq1[i] + remaining_substring(seq1[1:], seq2[first_index+1:])
            else:
                return remaining_substring(seq1[1:], seq2)
    return ''


if __name__ == "__main__": 

    records = []

    for seq_record in SeqIO.parse('inputData/rosalind_input_lcsq.txt', "fasta"):
        records.append(seq_record.seq)

    print(LCSLength(records[0],records[1]))
