fname = input("Enter file name: ")
fh = open(fname)

count = 0

for line in fh:
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '):
        continue
    words = line.split()
    #print(words)
    count = count + 1
    #print(count)
    mails = words[1]
    print(mails)

print("There were", count, "lines in the file with From as the first word")
