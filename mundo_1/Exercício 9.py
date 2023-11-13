# Make a program to show a number's multiplication table

try:  # The program will try running
    num = int(input("Type a number: "))  # The user should type an int type value
except ValueError:  # If the user type an invalid type value, it will run this part
    print('Invalid Value. Try again.')
else:  # But, if the user type a correct type of value, the program will continue running this part
    print('-' * 20)
    print('{} * {:2} = {}'.format(num, 1, num))
    print('{} * {:2} = {}'.format(num, 2, num*2))
    print('{} * {:2} = {}'.format(num, 3, num*3))
    print('{} * {:2} = {}'.format(num, 4, num*4))
    print('{} * {:2} = {}'.format(num, 5, num*5))
    print('{} * {:2} = {}'.format(num, 6, num*6))
    print('{} * {:2} = {}'.format(num, 7, num*7))
    print('{} * {:2} = {}'.format(num, 8, num*8))
    print('{} * {:2} = {}'.format(num, 9, num*9))
    print('{} * {:2} = {}'.format(num, 10, num*10))
    print('-' * 20)
