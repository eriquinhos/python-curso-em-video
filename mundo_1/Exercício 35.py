# Make a triangle analyser through its sides
from math import fabs
from time import sleep
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
a = float(input('First segment: '))
b = float(input('Second segment: '))
c = float(input('Third segment: '))
print('ANALYZING... PLEASE WAIT ...')
sleep(3)
if fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b:
    print('These segments CAN make a triangle!')
else:
    print("These segments CAN'T make a triangle!")
