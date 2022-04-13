#!/usr/bin/env python3

""" Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output
Rosalind_0808
60.919540

"""

__author__ = "T-Chinsky"
__copyright__ = "Copyright 2022"
__credits__ = ["T-Chinsky"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "T-Chinsky"
__status__ = "Completed"

def gc_content(seq):
    """
    return the GC content of a sequence
    :param seq: string of bases
    :return: number rounded to the thousandths place
    """
    percentGC = round(((seq.count('G') + seq.count('C'))/len(seq) * 100),6)
    return percentGC

def fastaDict(file):
    """
    open file and parse through adding each fasta sequence to dictionary
    :param file: filename to open
    :return: dictionary of fasta IDs and sequences
    """
    with open(file,'r') as fin:
        fasta_dictionary = {}
        for line in fin:
            line = line.strip()
            if '>' in line:
                seq_name = line[1:]
                if seq_name not in fasta_dictionary:
                    fasta_dictionary[seq_name] = ""
                continue
            else:
                fasta_dictionary[seq_name] += line

    fin.close()

    return fasta_dictionary

def getHighGC(fasta_dictionary):
    """
    takes in the fasta dictionary and gets the highest GC content sequence
    :param fasta_dictionary: dictionary of fasta sequences
    :return: sequence name and GC percentage
    """
    gcDict = {key: gc_content(value) for (key,value) in fasta_dictionary.items()}

    maxGC = max(gcDict, key = gcDict.get)

    print(maxGC + '\n' + str(gcDict[maxGC]))

if __name__ == '__main__':
    file = "rosalind_gc.txt"
    fDict = fastaDict(file)
    getHighGC(fDict)



