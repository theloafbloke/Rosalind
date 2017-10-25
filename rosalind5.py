file = open("rosalind_ini6.txt", "r")

f = file.read()

dict = {}
for word in f.split(' '):
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for key, value in dict.items():
    print str(key) + ' ' + str(value)
