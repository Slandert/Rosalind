"""
Rosalind problem rstr: http://rosalind.info/problems/rstr/

Author: Michael Ayars

Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”),
then at least one of the strings equals s.  We allow for the same random string to be created more than once.
"""



def probability_of_motif(string_number, gc_content, motif):
    """
    string_number : positive integer N <= 100000 potential number of random DNA strings
    gc_content : number between 0 and 1
    motif : string of DNA characters of at most 10 bp

    """
    motif_length = len(motif)

    gc_number = motif.count('G') + motif.count('C')
    at_number = motif_length - 1 - gc_number

    motif_probability = ((gc_content*0.5)**gc_number) * ((1-gc_content)*0.5)**at_number

    return (1.0 - (1.0 - motif_probability)**(1.0*string_number))
            
    
if __name__ == "__main__":

    with open('inputData/rosalind_input_RSTR.txt') as f:
        firstLine = f.readline().split()
        secondLine = f.readline()

      
    print(probability_of_motif(int(firstLine[0]), float(firstLine[1]), secondLine))
    
