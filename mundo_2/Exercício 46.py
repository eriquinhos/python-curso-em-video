# Write a program to countdown from 10 to 0 in a explosion!
from time import sleep
for c in range(10, 0, -1):
    print(c, end=' → ')
    sleep(1)
print('BOOM!!!')
print('The bomb has been exploded!')