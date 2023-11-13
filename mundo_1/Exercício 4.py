# Make a program to read something on the screen and tell the type and all the information about it

# First method:

a = input('Type something: ')  # The user will type something to check the information about the variable

print("What is its type? ", type(a))  # Shows the type of variable (string, int, float, ...)
print("Is that a number? ", a.isnumeric())  # True if the string is a numeric string, False otherwise.
print("Is that alphabetic? ", a.isalpha())  # True if the string is an alphabetic string, False otherwise.
print("Is that alpha-numeric? ", a.isalnum())  # True if the string is an alpha-numeric string, False otherwise.
print("Is that made of spaces?", a.isspace())  # True if the string is a whitespace string, False otherwise.
print("Is that all in upper letters? ", a.isupper())  # True if the string is an uppercase string, False otherwise.
print("Is that all in lowercase letters? ", a.islower())  # True if the string is a lowercase string, False otherwise.
print("Is that title-cased? ", a.istitle())  # True if the string is a title-cased string, False otherwise.

# Second method:

b = input('Type something: ')  # The user should type anything for the program to analyse
print("The type of {} is {}.".format(b, type(b)))  # Prints the type of the variable b
if b.isnumeric():
    print("{} is a number.".format(b))  # If b is a number, it will print the message
else:
    print("{} is not a number.".format(b))  # If it is not, the program will show you that it is not a number
if b.isalpha():
    print("{} is alphabetic.".format(b))   # If b is an alphabetic string, it will print the message
else:
    print("{} is not alphabetic.".format(b))  # If it is not, the program will show that it is not alphabetic
if b.isalnum():
    print("{} is alpha-numeric.".format(b))  # If b is alpha-numeric, it will print the message
else:
    print("{} is not alpha-numeric.".format(b))  # If it is not, it will show that on the screen
if b.isspace():
    print("{} is made of spaces.".format(b))  # If the string is made of spaces, it will print the message
else:
    print("{} is not made of spaces.".format(b))  # If it is not, it will show that on the screen
if b.isupper():
    print("{} is all in capital letters.".format(b))  # If the string is an uppercase string, it will print the message
else:
    print("{} is not all in capital letters.".format(b))  # If it is not, it will show that on the screen
if b.islower():
    print("{} is all in lowercase letters.".format(b))  # If the string is a lowercase string, it will print the message
else:
    print("{} is not all in lowercase letters.".format(b))  # If it is not, it will show that on the screen
if b.istitle():
    print("{} is title-cased.".format(b))  # If the string is a title-cased string, it will print the message
else:
    print("{} is not title-cased.".format(b))  # If it is not, it will show that on the screen
