# Make a program to calculate how much you will pay for a rented car
# It costs R$60.00 a day and R$0.15 per km

from functions.usable import isnumber

valid = False
while True:
    days = input('For how many days you rented this car? ')  # Days should be an int type number, while kilometers can
    kilometers = input('How many kilometers do you rode? ')  # be both int or float type
    if days.isnumeric() and isnumber(kilometers):  # If the typed values are correct they will be converted
        days = int(days)
        kilometers = float(kilometers)
        valid = True  # And now they're valid
    else:  # If it's not, the user will have to type it again
        print('Sorry, you typed a invalid value. Please, try again!')
    if valid:  # When both values are valid, the loop will break
        break

price = (60 * days) + (0.15 * kilometers)  # It will calculate the final price
print("You'll pay R${:.2f} for the car".format(price))  # And print it
