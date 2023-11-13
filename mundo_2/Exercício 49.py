# Write a program to show a multiplication table
mult = int(input('Type the number you want to multiplicate: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(mult, c, mult * c))
