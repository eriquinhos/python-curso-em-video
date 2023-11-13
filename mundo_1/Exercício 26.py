# Make a program to show: How many A letters it has? Whats the position of the first and the lats A letter.
phrase = str(input('Type a phrase: ')).strip().upper()
if 'A' in phrase:
    print('The phrase has {} A letters!'.format(phrase.count('A')))
    print('The first A showed in the position {}'.format(phrase.find('A') + 1))
    print('the last A showed in the position {}'.format(phrase.rfind('A') + 1))
else:
    print('The phrase do not have A letters')

