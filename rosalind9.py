from Bio import SeqIO


quality_list = []
for record in SeqIO.parse("rosalind_phre.txt", "fastq"):
    qc_average = int(sum(record.letter_annotations["phred_quality"]) / (len(record.letter_annotations["phred_quality"])))
    quality_list.append(qc_average)
count = 0

print quality_list
threshold = int(raw_input("Threshold: "))
for score in quality_list:
    if (score < threshold) == True:
        count +=1

print len(quality_list)
print count
