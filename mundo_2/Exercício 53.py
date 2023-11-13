# Escreva um progrma que consiga identificar palíndromos
word = str(input('Digite uma frase: ')).strip().upper()
parts = word.split()
together = ''.join(parts)
upside = ''
for c in range(len(together) - 1, -1, -1):
    upside += together[c]
if upside == together:
    print('A frase {} ao contrário fica {}, portanto é um PALÍNDROMO!'.format(word, upside))
else:
    print('A frase {} ao contrário fica {}, portanto NÃO é um PALÍNDROMO!'.format(word, upside))