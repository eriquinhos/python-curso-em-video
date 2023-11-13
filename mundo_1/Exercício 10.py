# Make a program to convert R$ to US$, € and £

try:
    money = float(input('How much do you have? R$'))  # The user should type the amount of money it wants to exchange
except ValueError:
    print('Invalid Value. Try Again.')  # This message will only appear if the user types a invalid value
else:  # if everything is ok, the money will be converted
    print('You can buy US${:.2f}, €{:.2f} or £{:.2f} '.format(money/5.57, money/6.12, money/6.83))
