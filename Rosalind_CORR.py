from Bio import SeqIO
from Bio import Seq
from itertools import combinations
#import collections

def compute_hamming_distance(s1, s2):
    #hamming distance is the number of mismatched characters between 2 strings of equal length

    return sum(b1 != b2 for b1, b2 in zip(s1, s2))


def detect_error_reads(reads):
    #takes in a list of reads of equal length.  Reads that match no other read (natively or in reverse complement) are erroneous reads with a hamming distance of 1 from
    #a correct read (or its reverse complement).  First splits the list into correct reads and error reads, then matches each error read (by hamming distance = 1) to a correct read (or RC)
    #and prints error read->correct read.
    
    reads = sorted(reads)
    correct_reads =[]
    
    for s1,s2 in combinations(reads, 2):
        if s1 == s2 or s1.reverse_complement() == s2:
            correct_reads.append(s1)
            correct_reads.append(s2)

    
    error_reads = set(reads) - set(correct_reads)

    for error in error_reads:
        for correct in correct_reads:
            if compute_hamming_distance(str(error), str(correct)) == 1:
                print(error + "->" + correct)
                break
            
            elif compute_hamming_distance(str(error), str(correct.reverse_complement())) == 1:
                print(error + "->" + correct.reverse_complement())
                break
    

if __name__ == "__main__":

    records = []
    
    for seq_record in SeqIO.parse('inputData/rosalind_input_corr.txt', "fasta"):
        records.append(seq_record.seq)

    detect_error_reads(records)
