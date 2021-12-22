largest = None
smallest = None

while True:
    sVal = input('Enter a number: ')
    if sVal == 'done':
        break
    try:
        iVal = int(sVal)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest = iVal
    elif iVal > largest:
        largest = iVal

    if smallest is None:
        smallest = iVal
    elif iVal < smallest:
        smallest = iVal

print('Maximum is', largest)
print('Minimum is', smallest)
