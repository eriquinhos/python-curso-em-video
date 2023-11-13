# Faça um programa que calcule Fatorial
print('Calculadora de Fatorial (!)')
num = int(input('Digite um número: '))
fat = 1
print(f'Calculando {num}!')
while num > 0:
    print(f'{num}', end='')
    print(' x 'if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print(fat)
