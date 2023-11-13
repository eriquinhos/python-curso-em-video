# Calculate the hypotenuse of a triangle from its cathetus

# There are two ways to solve this problem
from math import hypot  # Since this exercise is about importing modules, we will import this function
from functions.usable import isnumber

valid = False
while True:
    firCat = input("Length of the first cathetus: ")  # The user should type the cathetus' length in any unit
    secCat = input("Length of the second cathetus: ")
    # It is important here that both of the measures have to be in the same unit
    if isnumber(firCat) and isnumber(secCat):
        firCat = float(firCat)   # If the typed values are numbers, they will be converted to float type
        secCat = float(secCat)
        valid = True
    else:  # If it is not, the user will have to type it again
        print('Sorry, you typed invalid values. Please, try again.')
    if valid:  # And since the numbers are valid, the loop will end
        break

# First method, by using simple Pythagoras' Theorem:
hip = (secCat ** 2 + firCat ** 2) ** (1 / 2)

# Second method, using the hypot() function:
hyp = hypot(secCat, firCat)

# The program here should print the same values
print("The hypotenuse value is {}l.u.".format(hip))  # l.u.: length unit

print("The hypotenuse value is {}l.u.".format(hyp))
