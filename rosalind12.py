from Bio import SeqIO



threshold = 25
list_of_lists = []
count = 0
for record in SeqIO.parse("rosalind_bphr.txt", "fastq"):
    phred = record.letter_annotations["phred_quality"]
    list_of_lists.append(phred)

sum_list = [sum(i) for i in zip(*list_of_lists)]

for i in sum_list:
    avg = float(i)/float(len(list_of_lists))
    if (avg < threshold) == True:
        count += 1
print count
