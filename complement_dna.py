#!/usr/bin/env python3

""" Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT

"""

__author__ = "T-Chinsky"
__copyright__ = "Copyright 2022"
__credits__ = ["T-Chinsky"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "T-Chinsky"
__status__ = "Completed"

def reverseComp(dna, complement):
    """
    takes in a DNA string and prints the reverse complement
    :param dna: strand of DNA
    :param complement: dictionary to obtain complement bases
    :return: string of dna
    """
    seq = ""

    for i in reversed(dna):
        seq += complement.get(i,i)      #adds complement bases to new DNA string

    print(seq)


if __name__ == '__main__':
    dna = "GCCCAGATTATGCACCACCGAATGCGGAGTAAACCGCCAGATTAATGGACGTGACCACCCATAGCTTTCCTAACTCGAAACGGCAACACGGGAGTACCTGGATCATGGACCGAGCGTCCCAGGCCCCTGGAGGTTTTATAGCATGACTCTTGGGCCCACTCCGCATAAACGGATTAAGTCCCGTCGTGCCGAGTTTAGTTAACGGCCGTAGATCTAGTACGCTACCCATTGCCACCTGGTTCTTATTTCTCACGTCATTGAGAAGACGCGCACGCAAGTGAAGTACCGTCGACCACACCAGGTTCATACTAGTCTAACTCACAGACGGAGCCAATATTTCCGATGATCCTTTTTCCCTTTTTGATAGCGAGCATCGTAGCGACGGTATATTAGGTTGAACTCCGTGCTCATATCCTTGTTCTTGGACATACATCAAGTGATCCATTTCATCGTTACGGCTGGCGATCTGTAGACGCTCTGTGACCCGGGCTCGACGGTGCATGCACAGAGCTGAAGGTCTAGCGGTAGGGCTCACAAACGAATGTAGAAGAACGCAACCGACTTTAGCCCAAACTCATCTGAAAAAGTACCAATAATCTAGAGGAAATACGTTGATCCCTGTAATGACTAGTGGGATCTAGTACGAACCCAATTCGAAGGAACAGACTTCTCAATATACTGCAGCATGATTTTGCTTAGCCATTTAATTGTATTCGAGGACCCTTCGAAATTCTACTTATAAATTGCCAAACCCTTATGGAGGCGTGTGGGGGCAGAAAGGGCACGCGTCCACACTGACAGAAAGCACCACAGAAACCATAAATCTTTTAGAGCAACGCGATGTTCAAACCGTAGGTGTGACGGATTCATTGCGACGACCGTCCGGTCAAGCCACCGTAAGTTTGGGGAGCTTGGGATATGGTATGTTGAGAGCGCACCTAGTCGATCACTCCCTCTG"
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverseComp(dna,complement)