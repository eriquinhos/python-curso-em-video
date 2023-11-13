# Make a program that convert meters to km, hm, dam, dm, cm and mm

try:
    space = float(input('Type a distance [m]: '))  # The user should type an int/float type value

    print('The distance {}m is equal to:'.format(space))
    print('{}km'.format(space*10**(-3)))  # It will show the distance in kilometers
    print('{}hm'.format(space*10**(-2)))  # It will show the distance in hectometers
    print('{}dam'.format(space*10**(-1)))  # It will show the distance in dekameters
    print('{}dm'.format(space*10))  # It will show the distance in decimeters
    print('{}cm'.format(space*10**2))  # It will show the distance in centimeters
    print('{}mm'.format(space*10**3))  # It will show the distance in milimiters

except ValueError:
    print('Invalid value. Please, try again.')
