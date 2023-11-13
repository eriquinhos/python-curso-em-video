pares = []
impares = []
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os números pares digitados foram: {sorted(pares)}')
print(f'Os números ímpares digitados foram: {sorted(impares)}')
