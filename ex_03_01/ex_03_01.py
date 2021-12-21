hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

if hours > 40:
    pay_reg = hours * rate
    pay_ot = (hours - 40.0) * (rate * 0.5)
    print('Pay:', pay_reg + pay_ot)
else:
    pay_reg = hours * rate
    print('Pay:', pay_reg)
