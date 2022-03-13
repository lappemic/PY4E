fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"
fh = open(fname)

import re

numlist = list()

for line in fh:
    line = line.rstrip()
    all = re.findall('[0-9]+', line)
    if len(all) < 1: continue
    for i in all:
        num = int(i)
        numlist.append(num)

#print(numlist)

summed = sum(numlist)
print(summed)
