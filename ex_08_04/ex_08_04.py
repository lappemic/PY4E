fname = input("Enter file name: ")
fh = open(fname)
#fh = open('romeo.txt')
lst = list()
for line in fh:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)

    for wd in wds:
        #print(wd)
        if wd not in lst:
            lst.append(wd)

#print(lst)
lst.sort()
print(lst)
