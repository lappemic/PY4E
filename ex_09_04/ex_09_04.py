fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

counts = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    #print(words)
    emails = list()
    emails.append(words[1])
    #print(emails)
    for email in emails:
        counts[email] = counts.get(email, 0) + 1

#print(counts)

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
