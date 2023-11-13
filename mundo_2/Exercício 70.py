print('---' * 20)
print('{:^60}'.format(' ARMAZÉM DO SEU BARATA '))
print('---' * 20)
nome = cont = pr_Menor = ''
total = produto = mais1000 = major = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    price = float(input('Preço: R$'))
    total += price
    produto += 1
    if price > 1000:
        mais1000 += 1
    if produto == 1:
        pr_Menor = nome
        minor = price
    else:
        if price < minor:
            pr_Menor = nome
            minor = price
    cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont =='N':
        print('{:-^60}'.format('FIM DO PROGRAMA'))
        break
print(f'O total da compra for de R${total:.2f}.')
print(f'Temos {mais1000} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {pr_Menor} de R${minor:.2f}')
