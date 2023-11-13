# Escreva um programa em que peça o ano de nascimento de x pessoas e diga quantos são maiores de idade
from datetime import datetime
nP = int(input('Número de pessoas a serem analisadas: '))
major = 0
minor = 0
for c in range(1, nP + 1):
    date = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if datetime.today().year - date >= 18:
        major += 1
    else:
        minor += 1
print('Nesse grupo, há {} pessoas maiores de idade'.format(major), '\n', 'E também há {} menores de idade'.format(minor))