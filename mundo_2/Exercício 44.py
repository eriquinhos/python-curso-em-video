# Lojas Eriquinhos
print('-=-' * 20)
print('\033[01m', 'LOJAS ERIQUINHOS')
print('\033[0;0m', '-=-' * 20)
price = float(input('Preço das Compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista em dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
option = int(input('Qual é a opção? '))
if option == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(price, price * 0.9))
elif option == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(price, price * 0.95))
elif option == 3:
    print('Cada parcela da sua compra de R${:.2f} será de R${:2f}.'.format(price, price/2))
    print('O preço final da compra não foi alterado!')
elif option == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(parcela, (price * 1.2)/parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, price * 1.2))
else:
    print('Opção inválida. Tente novamente!')