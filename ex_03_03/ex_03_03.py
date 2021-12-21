sScore = input('Enter score between 0.0 and 1.0: ')

try:
    fScore = float(sScore)
except:
    print('Bad score')
    quit()

if fScore > 1.0 or fScore < 0.0:
    print('Bad score')
else:
    if fScore >= 0.9:
        print('A')
    elif fScore >= 0.8:
        print('B')
    elif fScore >= 0.7:
        print('C')
    elif fScore >= 0.6:
        print('D')
    else:
        print('F')
