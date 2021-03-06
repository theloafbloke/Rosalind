from Bio import SeqIO

def hammingDistance( s1, s2 ):
    sum = 0
    for i in xrange(len(s1)):
        if s1[i] != s2[i]:
            sum += 1
    return sum

s = "AGATTTGGTTCTAGCAATGTCCGGGGCTCTCCATGTGTAGCTTCTACGGTTAGAGTCGGTGTCTGGGACTACCCTCATATTACTTCTACGGTTAGAGTCGGTGTCTGGGACTACCACCAGCCGGCGTTTTAGCCTCGTGACTAAGTACAGCGCTCATAGAAGAGTAGCATGTTCTAGATGACGAGTATCTACGGTTAGAGTCGGTGTCTGGGACTACCCCGGGGAGGCTGTCTACGGTTAGAGTCGGTGTCTGGGACTACCTTAGTCCATATTGGCATACCCAGTAGGAAGCCTACAGGACGAATTGTACTGCAACTAAATGGTATCAAGACGGGTATAGTATCAAAATAATTAAGTCCAAGGCTCAAGAGATGGTAGGGAAAAGATAGGTCGTAAAGAGACGCCACCCAGGGGCGATTCCTCGCCGCGTTATACAAGCCCTGTTCCCTTGCGAAACGCGGCACAGCGCCGTCGCGTTGGGATTTCTACGGTTAGAGTCGGTGTCTGGGACTACCTCCGCGCCATGTGCCGCAGTTTAGTCGGCACCTCACGCTCACCAATAGACTATTAGTTCTACGGTTAGAGTCGGTGTCTGGGACTACCGAGGATAGGGATGAGCCGGTCTACCAGTATAACGTTCTCAACGTGACTTATGAGCATCAGTAATTCCGCCTTTTTGGTTCATGTAAATTCTTCAGCCAGCCTTTCCTACGGTTAGAGTCGGTGTCTGGGACTACCGCAAATTCCTCCCTCATGACATTGCGCTGTACGAACTATGAGTGCCCTTCCACGATGTGACATCGCCAGTGTCCTGGGGTTGCTCGCAAAACGAATACTATGACATTCACTTGGTATCTCCGAAAGATATGAGTCTATGTCTTGCCCGCTCTGCGAACTGCTATTTTCATCCCCGACTGGACA"

t ="TGGCTTGATGTAGGCCTGATGCGCAGTCGGTAAGGATGACTTGAGTCAGGTTCTACGGTTAGAGTCGGTGTCTGGGACTACCGGTAATGCGGTTCTACGGTTAGAGTCGGTGTCTGGGACTACCTTGGCTCATCTCTACGGTTAGAGTCGGTGTCTGGGACTACCGTGTTTGTTGACCACCGTTTTAGTTCTACCGTCGCGAATTTCTGCTAGATGTAAGCATGTGCTATGTGACGTTTGTAGAACCTAAACCTAGGTGTTGTGGGCATACAACCCAACACCGAATGAATGTTAGCGCTAGCGGAAGAACTGTAACTAGAACTGCTTACGAGGTGTAGTCGAAGCTCATCACGGGCCGTCGCTTGGTAGATGCTATCAGCAGGGCGGACAACGTGTTTCAAAAAAGATAGCGAGGACTGTTTCCTAGCCTTACCCTTTAGTTATGTCAAAGTTTCCAGGCACATGTAGATTCGACGGCATCGAATTCTGATATAGTGGGATGCACCCGGGTGACTCATCCTCCACCGCAAATCTTGTTCGTCAGCTCAGTCTAACATGATCTACGTGCTCGAGTCGGTCTCTACGGTTAGAGTCGGTGTCTGGGACTACCAACGGCCATAGCATATGTGTTGAGATCCACTCCCACTGGAGGCGCCCTGGACTCCGTTCGACCTATCAAACCAGAATGCCTTAGGTCACTAGATGTTGAACTCGGACATGAAGAGGCGGATATACGCATGTCGGATTCACTGCTTATTGTCACCCGAAGAGGCGAAGGGCCATGTGCTTCCGTCCAGCGGTAAAACGAGTCTCGGACTGCACGTGAAGTATGCAGGTTCTAGAGAAACTTGGAACAGAGTCTTAGTGAGTCCGGACCCTACGCATATACAGCGCCAGATTTGGGTAGTTAATCAAGGGGAGTCTTCTACGGTTAGAGTCGGTGTCTGGGACTACCTCCTTTCGTC" # pick r as the alignment with
r = "TTCTACGGTTAGAGTCGGTGTCTGGGACTACCTCC"
seqs = [s,t]
count = 0
for x in range(2):
    count = 0
    curr = seqs[x]
    for i in range(len(curr)-len(r)):
        str = curr[i:i+len(r)]
        if hammingDistance(str,r) <= 3:
            count += 1
    print count,
