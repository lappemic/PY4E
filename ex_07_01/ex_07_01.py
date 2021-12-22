fileName = input('Enter a file name: ')
try:
    fHand = open(fileName)
except:
    print('File cannot be opened: ', fileName)
    quit()

for line in fHand:
    lineStripped = line.rstrip()
    print(lineStripped)
