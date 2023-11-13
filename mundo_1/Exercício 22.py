# Make a program that shows a name in upper, lower, the lenght of the first and the whole name

name = str(input('Type your name: ')).strip()
print('Your name is {}'.format(name))
print('Your name in upper letters is {}'.format(name.upper()))
print('Your name in lower is {}'.format(name.lower()))
print('Your name has {} letters'.format(len(name) - name.count(' ')))
n = name.split()
print('Your first name {} has {} letters'.format(n[0], len(n[0])))