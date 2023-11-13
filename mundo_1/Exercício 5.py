# Make a program that tells the successor and the processor of a number

try:  # The program will try running
    num = int(input('Type a number: '))  # The user should type an int type value
    suc = num + 1  # When you add 1 to a number, it will be its successor
    pro = num - 1  # When you subtract 1 to a number, it will be its processor
    print('The successor of {} is {} and the processor is {}.'.format(num, suc, pro)) # It will print the three values
except ValueError:  # If the user type another type of variable, string or float, for example, it wil run the next lines
    print('You typed an invalid value. Please, try again.')
