# Make a program to show the order of a presentation
import random
firstName = str(input('Type a name:'))
secondName = str(input('Type a name: '))
thirdName = str(input('Type a name: '))
fourthName = str(input('Type a name: '))
lis = [firstName, secondName, thirdName, fourthName]
random.shuffle(lis)
print('A ordem de apresentação será: ')
print(lis)
