# Make a program to calculate the area of a wall and how much paint you will need to paint it
# 1L of paint = 2m²

try:  # In this part, the user should type the values of HEIGHT and length of the single wall it wants to paint
    height = float(input('Type the HEIGHT of your wall: '))
    length = float(input('Type the length of your wall: '))
except ValueError:  # If one of the values are not valid, the message below must appear on the screen
    print('Invalid Value. Please, try again.')
else:
    print('The area of the wall is {}m²'.format(length*height))  # So, the program will calculate the area
    print('Therefore, you will need {}L of paint'.format((length*height)/2))  # And how much paint the user needs
