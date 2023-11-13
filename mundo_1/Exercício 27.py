# Make a program to show a person's first and last name
name = str(input('Type a name: '))
n = name.split()
print('Your name is: {}'.format(name))
print('Your first name is: {}'.format(n[0]))
print('Your last name is: {}'.format(n[len(n) - 1]))
