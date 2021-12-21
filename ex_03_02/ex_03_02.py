sHours = input('Enter hours: ')
sRate = input('Enter rate: ')

try:
    fHours = float(sHours)
    fRate = float(sRate)
except:
    print('Error, please enter numeric input')
    quit()

if fHours > 40:
    pay_reg = fHours * fRate
    pay_ot = (fHours - 40.0) * (fRate * 0.5)
    print('Pay:', pay_reg + pay_ot)
else:
    pay_reg = fHours * fRate
    print('Pay:', pay_reg)
