from Bio import Entrez
from Bio import SeqIO
file = open("rosalind_frmt.txt", "r")
f = file.read()
id_list = []
for word in f.split(' '):
    id_list.append(word)

Entrez.email = "collin.lucken@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

for i in range(0, len(id_list)):

    print records[i].id
    print len(records[i].seq)
