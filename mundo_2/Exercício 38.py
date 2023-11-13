# Write a program to compare numbers
num_1 = float(input('Type a number: '))
num_2 = float(input('Type another number: '))
if num_1 > num_2:
    print('{} is bigger than {}!'.format(num_1, num_2))
elif num_1 < num_2:
    print('{} is bigger than {}!'.format(num_2, num_1))
else:
    print('{} and {} are the same number!'.format(num_1, num_2))
