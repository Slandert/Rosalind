"""
Rosalind problem lexv: http://rosalind.info/problems/lexv/

Author: Michael Ayars

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically.
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

"""


def alphabetize(letters, n, cur = '', result=[]):
    if n > 0:
        for char in letters:
            result.append(cur + char)
            alphabetize(letters, n-1, cur + char, result)
        return result


def ordered_permutations_of_string(seq, n):
    letters = seq.split()
    return alphabetize(letters, n)

   


if __name__ == "__main__":
    
    input_seq = 'Q N Z V K I H T D A E M'
    max_length = 4

    print('\n'.join(ordered_permutations_of_string(input_seq, max_length)))
