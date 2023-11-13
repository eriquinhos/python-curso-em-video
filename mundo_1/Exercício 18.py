# Calculate sin, cos and tg of an angle
import math  # Since we are going to use plenty of functions, we can simply import the whole module
from functions.usable import isnumber

valid = False
while True:
    ang = input('Type an angle (in degrees): ')  # The user should type a angle in degrees. Ej: 60º or 250.5º == 250º30'
    if isnumber(ang):
        ang = float(ang)  # If it is a number, it will be converted to float type
        valid = True
    else:
        print('You typed an invalid value. Please, try again!')  # If it is not, the message will appear
    if valid:
        break  # Valid == Loop breaks
# Print sin, cos, tg
print('The SINE of {} is {:.2f}!'.format(ang, math.sin(math.radians(ang))))
print('The COSINE of {} is {:.2f}!'.format(ang, math.cos(math.radians(ang))))
print('The TANGENT of {} is {:.2f}!'.format(ang, math.tan(math.radians(ang))))
