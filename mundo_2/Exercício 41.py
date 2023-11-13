# Escreva um programa para classificar os atletas em categorias
from datetime import date
year = int(input('Digite o ano do seu nascimento: '))
age = date.today().year - year
if age <= 9:
    print('O atleta tem {} anos!'.format(age))
    print('Classificação: MIRIM')
elif 9 < age <= 14:
    print('O atleta tem {} anos!'.format(age))
    print('Classificação: INFANTIL')
elif 14 < age <= 19:
    print('O atleta tem {} anos!'.format(age))
    print('Classificação: JÚNIOR')
elif 19 < age <= 25:
    print('O atleta tem {} anos!'.format(age))
    print('Classificação: SÊNIOR')
else:
    print('O atleta tem {} anos!'.format(age))
    print('Classificação: MASTER')