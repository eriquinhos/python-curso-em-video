# Analisador de triângulos v2.0
from math import fabs
from time import sleep
print('-=-' * 20)
print('TRIANGLE ANALYSER 2.0')
print('-=-' * 20)
a = float(input('First segment: '))
b = float(input('Second segment: '))
c = float(input('Third segment: '))
print('ANALYZING... PLEASE WAIT ...')
sleep(3)
if fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b and a == b == c:
    print('These segments CAN make an EQUILATERAL TRIANGLE!')
elif fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b and a == b != c or b == c != a or a == c != b:
        print('These segments CAN make an ISOSCELES TRIANGLE!')
elif fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b and a != b != c:
    print('These segments CAN make a SCALENE TRIANGLE!')
else:
    print("These segments CAN'T make a triangle!")