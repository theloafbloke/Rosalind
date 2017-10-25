from Bio import SeqIO


for record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    seq = record.seq
    seq_len = float(len(seq))
    gc_content = float(0)

    for base in seq:
        if base == 'G':
            gc_content += 1
        elif base == 'C':
            gc_content +=1
        else:
            pass
        gc_average = gc_content/seq_len
    print "Read %s has GC content: %s" %(record.id, gc_average)
