file = open("rosalind_ini5 (1).txt", "r")
f = file.readlines()
# create a list of even numbered lines in the text file
length = len(f)
LinesToWrite= []

for i in range(1, length, 2):
    LinesToWrite.append(f[i])



#write that list to a new file

o = open('output.txt', 'w')

for i in LinesToWrite:
    o.write(str(i))

o.close()
