# Write a program to tell someone if they're ready to join the army
from datetime import date
born = int(input('Your birth year: '))
age = date.today().year - born
if age == 18:
    print('Who born in {} will be {} years old in {}'.format(born, age, date.today().year))
    print('You MUST join the army NOW!!')
elif age > 18:
    print('Who born in {} will be {} years old un {}.'.format(born, age, date.today().year))
    print('You had to join the army in {}'.format(born + 18))
else:
    print('Who born in {} will be {} in {}'.format(born, age, date.today().year))
    print('You have to join the army in {}'.format(born + 18))
