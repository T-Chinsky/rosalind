Acount = 0
Ccount = 0
Gcount = 0
Tcount = 0

dna = "CACAAATCAAAGCTTCCGGAAGACATTGTAACTACTTGCCACCACCCCCACATAAGGACGGGGCGTGTGGCGTACAAGTGAAATGGGATCAGTGTGCATTAACTCCTTACTTCTTATTATTGGCTAGCACATTGAGCATACTGGGACGGGTTAGAACGGGGTGTTTCAGAATGCCAGGCTACCTCCGAGGTCGAGAAATACCAGTGCCGTGTGACATATTCCGTAATCGGCGTAGCTCTGCTGGTGTGTCTCGTTCTAACGTGCCGGAACATTCGCATTATTCCGGCGTGACACCCGAGGCACCGATAGCTAAAGAAGCGTTAATAGGAACGTGCTAAACCTTCCACCCTGACTGGCCTTCAATACATTGGTCCCCATCAATGTGGCTGGGCGCAGGCGCTAAAAACCAAAACGTGGTGCCAGAACGCCAAAAGCGTACTGTGATATAGCATAACGTTACCTATACTCGAACACGTGTTCGGATCATGAACTATAGTAAAAGCCTCGCAATTCCTCTACTGTCGGATCACAACATACCAAAGGAACTCATAGCCGTCGTAACCCCTTTTAACGTTGAACATATAAGTGAATTGAGCGATTAGTGTGAAGGTTCCAATAGTTATGTGGTGCCCCCTAACAGTCCACCGACTCACTCCCGAGCCACAATTATCGCATACTGCCGTAGATCCGACTATGGGTTATGTGATTTCTGATCACTACTGAGGCGACATTATATTAGAAGGTGTACGGGCATGTGTAAATCGCGCCTCAGAGGCGGGAGCGGGTACGGAGCCTCGTCACCCGCGCCGCACGTTTAATGACCCAGGCTTGGCTTCTCCTATTGTGTCCTTTTCCCTGACAACTTCACCCTGAGTGTTGCAGGTCCAGGGGTTTTCAGTGCTTTAATAGCATTGCTAGGATTGTGGGATTATTCACCGGTCTACCTCCCTAGAGTGG"

for i in dna:
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