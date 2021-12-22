fileName = input('Enter a file name: ')
try:
    fHand = open(fileName)
except:
    print('File cannot be opened: ', fileName)
    quit()

lineCount = 0
totNum = 0

for line in fHand:
    lineStripped = line.rstrip()
    if lineStripped.startswith('X-DSPAM-Confidence:'):
        # print(lineStripped)
        posCol = lineStripped.find(':')
        # print(posCol)
        sNum = lineStripped[posCol+1:]
        # print(sNum)
        fNum = float(sNum)
        # print(fNum)
        totNum = totNum + fNum
        # print(sumNum)
        lineCount = lineCount + 1
        # print(lineCount)

# print(lineCount)
print('Average spam confidence:', totNum/lineCount)

    #lineX = lineStripped.startswith('X-DSPAM-Confidence:')
