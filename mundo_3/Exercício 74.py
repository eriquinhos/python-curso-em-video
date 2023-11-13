from random import randint as ri
tupla = (ri(0, 100), ri(0, 100), ri(0, 100), ri(0, 100), ri(0, 100))
print('Os valores sorteados foram: ', end='')
for value in tupla:
    print(value, end=' ')
print(f'\nO maior valor sorteado foi: {max(tupla)}.')
print(f'O menor valor sorteado foi: {min(tupla)}.')