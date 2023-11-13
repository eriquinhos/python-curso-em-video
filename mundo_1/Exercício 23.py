# Faça um programa que mostre as unidades, dezenas, centenas e unidades de milhar de um número entre 0 e 9999
num = (int(input('Digite um número de até quatro dígitos: ')))
n = str(num)
if num <= 9:
    print('Analisando o número {}'.format(num))
    print('Unidades: {}'.format(n[0]))
elif 10 <= num <= 99:
    print('Analisando o número {}'.format(num))
    print('Dezenas: {}'.format(n[0]))
    print('Unidades: {}'.format(n[1]))
elif 100 <= num <= 999:
    print('Analisando o número {}'.format(num))
    print('Centenas: {}'.format(n[0]))
    print('Dezenas: {}'.format(n[1]))
    print('Unidades: {}'.format(n[2]))
elif 1000 <= num <= 9999:
    print('Analisando o número {}'.format(num))
    print('Unidades de milhar: {}'.format(n[0]))
    print('Centenas: {}'.format(n[1]))
    print('Dezenas: {}'.format(n[2]))
    print('Unidades: {}'.format(n[3]))
else:
    print('Esse número tem mais de quatro dígitos!')