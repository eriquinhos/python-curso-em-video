numeros = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        print('Valor adicionado com sucesso!')
        numeros.append(valor)
    else:
        print('Esse valor já foi digitado, portanto, não será adicionado!')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você digitou os valores {numeros.sort()}')
