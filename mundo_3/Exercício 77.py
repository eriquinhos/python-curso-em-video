vowels = ('a', 'e', 'i', 'o', 'u', 'y')
words = ('Juice', 'Hamburguer', 'Serendipity', 'Kitty', 'Puppy', 'Osmium', 'Canada', 'Power', 'Loving', 'Me', 'Is',
         'Losing', 'Game', 'Arcade')
for word in words:
    print(f'The vowels in {word.upper()} are: ', end='')
    for vowel in vowels:
        if vowel in word:
            print(f'{vowel} ', end='')
    print('\n')
