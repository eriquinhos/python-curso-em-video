numeros = []
for n in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {n}: ')))
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} na(s) posição(ões): ', end='')
for k, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{k} ', end='')
print(f'\nO menor valor digitado foi {min(numeros)} na(s) posição(ões): ', end='')
for k, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{k} ', end='')
