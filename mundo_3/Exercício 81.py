pares = []
impares = []
tudo = []
while True:
    n = int(input('Digite um valor: '))
    tudo.append(n)
    if n % 2 ==0:
        pares.append(n)
    else:
        impares.append(n)
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Os números digitados foram {sorted(tudo)}')
print(f'Os números PARES digitados foram {sorted(pares)}')
print(f'Os números ÍMPARES digitados forma {sorted(impares)}')