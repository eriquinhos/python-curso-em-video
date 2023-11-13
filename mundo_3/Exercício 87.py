matriz  = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma_Par = soma_Tres = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor do a{i+1}{j+1}: '))
        if matriz[i][j] % 2 == 0:
            soma_Par += matriz[i][j]
        if i == 1:
            if j == 1:
                maior = matriz[i][j]
            else:
                if matriz[i][j] > maior:
                    maior = matriz[i][j]
        if i == 2:
            soma_Tres += matriz[i][j]
print('-=-' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é de {soma_Par}.')
print(f'A soma dos valores da terceira linha é de {soma_Tres}.')
print(f'O maior valor da segunda linha é {maior}.')
