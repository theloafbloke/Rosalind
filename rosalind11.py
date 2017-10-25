from Bio import SeqIO

quality_list = []
threshold = 24

for record in SeqIO.parse("rosalind_filt.txt", "fastq"):
    qc_average = int(sum(record.letter_annotations["phred_quality"]) / (len(record.letter_annotations["phred_quality"])))
    base_quality = record.letter_annotations["phred_quality"]
    base_meets_score = 0
    for i in base_quality:

        if (i >= threshold) == True:
            base_meets_score += 1
    percent = float(base_meets_score)/float(len(base_quality))
    if (((percent >= .76) == True) and (qc_average >= threshold)):
        quality_list.append(record)
print len(quality_list)
