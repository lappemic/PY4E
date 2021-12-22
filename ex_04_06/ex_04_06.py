def computepay(hours, rate):
    '''
    Function to promt the user for hours and rate per hour
    using input to compute gros pay
    '''

    if hours > 40:
        pay_reg = hours * rate
        pay_ot = (hours - 40.0) * (rate * 0.5)
        pay_end = pay_reg + pay_ot
    else:
        pay_end = hours * rate
    return pay_end

sHours = input('Enter hours: ')
sRate = input('Enter rate: ')
fHours = float(sHours)
fRate = float(sRate)

pay_comp = computepay(fHours, fRate)

print('Pay', pay_comp)
