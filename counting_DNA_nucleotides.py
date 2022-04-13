#!/usr/bin/env python3

""" Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
20 12 17 21

"""

__author__ = "T-Chinsky"
__copyright__ = "Copyright 2022"
__credits__ = ["T-Chinsky"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "T-Chinsky"
__status__ = "Completed"

def nuceloCount(dna):
    """
    takes in a string of DNA and obtains the base counts for each pyrimidine and purine
    :param dna: string of nucleotides
    :return: integer count of each base
    """
    Acount = 0
    Ccount = 0
    Gcount = 0
    Tcount = 0
    for i in dna:           # checks for each base and adds to counter
        if i == 'A':
            Acount += 1
        elif i == 'C':
            Ccount += 1
        elif i == 'G':
            Gcount += 1
        elif i == 'T':
            Tcount += 1
        else:
            continue

    print(Acount,' ',Ccount,' ',Gcount,' ',Tcount)

if __name__ == '__main__':
    dna = "CACAAATCAAAGCTTCCGGAAGACATTGTAACTACTTGCCACCACCCCCACATAAGGACGGGGCGTGTGGCGTACAAGTGAAATGGGATCAGTGTGCATTAACTCCTTACTTCTTATTATTGGCTAGCACATTGAGCATACTGGGACGGGTTAGAACGGGGTGTTTCAGAATGCCAGGCTACCTCCGAGGTCGAGAAATACCAGTGCCGTGTGACATATTCCGTAATCGGCGTAGCTCTGCTGGTGTGTCTCGTTCTAACGTGCCGGAACATTCGCATTATTCCGGCGTGACACCCGAGGCACCGATAGCTAAAGAAGCGTTAATAGGAACGTGCTAAACCTTCCACCCTGACTGGCCTTCAATACATTGGTCCCCATCAATGTGGCTGGGCGCAGGCGCTAAAAACCAAAACGTGGTGCCAGAACGCCAAAAGCGTACTGTGATATAGCATAACGTTACCTATACTCGAACACGTGTTCGGATCATGAACTATAGTAAAAGCCTCGCAATTCCTCTACTGTCGGATCACAACATACCAAAGGAACTCATAGCCGTCGTAACCCCTTTTAACGTTGAACATATAAGTGAATTGAGCGATTAGTGTGAAGGTTCCAATAGTTATGTGGTGCCCCCTAACAGTCCACCGACTCACTCCCGAGCCACAATTATCGCATACTGCCGTAGATCCGACTATGGGTTATGTGATTTCTGATCACTACTGAGGCGACATTATATTAGAAGGTGTACGGGCATGTGTAAATCGCGCCTCAGAGGCGGGAGCGGGTACGGAGCCTCGTCACCCGCGCCGCACGTTTAATGACCCAGGCTTGGCTTCTCCTATTGTGTCCTTTTCCCTGACAACTTCACCCTGAGTGTTGCAGGTCCAGGGGTTTTCAGTGCTTTAATAGCATTGCTAGGATTGTGGGATTATTCACCGGTCTACCTCCCTAGAGTGG"
    nuceloCount(dna)