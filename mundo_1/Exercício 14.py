# Make a program to convert the temperature in ºC to ºF and K

from functions import usable  # From the 'functions' directory, import 'usable'

valid = False  # The typed number is not valid yet
while True:
    tCelsius = input('Type the temperature (ºC): ')  # The user should type a int/float type value
    if usable.isnumber(tCelsius):  # If the typed value is a number, it will be concerted to float type
        tCelsius = float(tCelsius)
        valid = True  # and it will become valid
    else:
        print('Invalid Number. Try Again!')  # If it's not, the error message will appear and the user should type
        # it again
    if valid:  # but if it is valid, the loop will end
        break
tFahrenheit = (((tCelsius/5) * 9) + 32)   # Converting the temperatures
tKelvin = tCelsius + 273

print('The temperature {}ºC corresponds to {:.1f}ºF and {:.1f}K'.format(tCelsius, tFahrenheit, tKelvin))
# And finally print them all
