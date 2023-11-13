lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
n = int(input('Digite um número para procurar na lista: '))
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista ao contrário fica {lista}')
if n in lista:
    print(f'O número {n} pertence à lista.')
else:
    print(f'O número {n} não pertence à lista.')