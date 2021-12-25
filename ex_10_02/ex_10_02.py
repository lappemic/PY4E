fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

counts = dict()
hourcounts = dict()

for line in fh:
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '):
        continue
    words = line.split()
    #print(words)
    timeStamp = words[5]
    #print(timeStamp)
    timeStampPieces = timeStamp.split(':')
    #print(timeStampPieces)
    hour = timeStampPieces[0]
    #print(hour)
    hours = list()
    hours.append(hour)
    # print(hours)
    for h in hours:
        hourcounts[h] = hourcounts.get(h, 0) + 1

#print(hourcounts)

lst = list()
for k, v in hourcounts.items():
    newtup = (k, v)
    lst.append(newtup)

#print(lst)

lst = sorted(lst)

#print(lst)

for k, v in lst:
    print(k, v)
