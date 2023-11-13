# Make a program to show the double, the triple and the square root of a number

from math import sqrt  # From the math repository, it will import the square root function
try:  # The program will try running this part of the code
    num = int(input('Type a number: '))  # The user should type and int type value

    print('The double of {} is {}'.format(num, num * 2))  # It will show the double of the number on the screen
    print('The triple of {} is {}'.format(num, num * 3))  # It will show the triple of the number on the screen
    print('The square root of {} is {:.2f}'.format(num, sqrt(num)))  # It will show the square root of the number

except ValueError:  # If the user does not type an it type value, ti will print this message on the screen
    print('You typed an invalid value. Please, try again.')

# Disclaimer: It is not necessary to import the sqrt function. You could just use 'num ** 0.5', that would give the same
# result
