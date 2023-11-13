print('=' * 20)
print('{:^20}'.format('BANCO DA PRAÇA'))
print('=' * 20)
value = int(input('Qual o valor você gostaria de depositar? R$'))
while True:
    if value >= 50:
        notas50 = value // 50
        value -= (50 * notas50)
        print(f'Total de {notas50} cédulas de R$50,00.')
    elif 50 > value >= 20:
        notas20 = value // 20
        value -= (20 * notas20)
        print(f'Total de {notas20} cédulas de R$20,00.')
    elif 20 > value >= 10:
        notas10 = value // 10
        value -= (10 * notas10)
        print(f'Total de {notas10} cédulas de R$10,00.')
    elif 10 > value > 0:
        notas1 = value // 1
        value -= notas1
        print(f'Total de {notas1} cédulas de R$1,00.')
        break
