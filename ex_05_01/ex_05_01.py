num = 0
tot = 0.0

while True:
    sVal = input('Enter a number: ')
    if sVal == 'done':
        break
    try:
        fVal = float(sVal)
    except:
        print('Invalid input')
        continue
    # print(fVal)
    num = num + 1
    tot = tot + fVal

# print('All done')
print(tot, num, tot/num)
