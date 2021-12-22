str = 'X-DSPAM-Confidence: 0.8475'

posCol = str.find(':')
#print(posCol)

sNum = str[posCol+1:]
#print(sNum)

fNum = float(sNum)
print('Converted string to float number:', fNum)
