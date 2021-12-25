fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "clown.txt"
fh = open(fname)

di = dict()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

#print(di)

#x = sorted(di.items()) # sorted alphabetically!
#print(x[: 5])

tmp = list()
for k, v in di.items():
    #print(k, v)
    newt = (v, k)
    tmp.append(newt)

#print('Flipped: ', tmp)

tmp = sorted(tmp, reverse = True)

print('Sorted: ', tmp[: 5])

print('Nicer way of printing them out:')
for v, k in tmp[: 5]:
    print(k, v)
