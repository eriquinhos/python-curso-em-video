# Make a program to show the integer part of a number
from math import trunc  # Import this function that truncates the Real x to the nearest Integral toward 0.
from functions.usable import isnumber

valid = False
while True:
    num = input('Type any number: ')  # The user should type any number, float or int
    if isnumber(num):
        num = float(num)  # If the typed value is a number, it will be turned into an float type
        valid = True
    else:  # If it's not, the message will appear and the user is going to type the value again
        print('Sorry, you typed an invalid number. Please, try again!')
    if valid:  # If it's valid the loop ends
        break
print('The integer part of {} is {}'.format(num, trunc(num)))  # Print the integer part
