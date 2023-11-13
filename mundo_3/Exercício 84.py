dados = []
pessoas = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados.copy())
    dados.clear()
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
for i, v in enumerate(pessoas):
    if i == 0:
        maior = v[1]
        menor = v[1]
    else:
        if v[1] > maior:
            maior = v[1]
        if v[1] < menor:
            menor = v[1]
print(f'O maior peso digitado foi {maior}kg de ', end='')
for i, v in pessoas:
    if v == maior:
        print(i, end=' ')
print()
print(f'O menor peso digitado foi {menor}kg de ', end='')
for i, v in pessoas:
    if v == menor:
        print(i, end=' ')
