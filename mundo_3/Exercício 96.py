def area(largura, comprimento):
    a = largura * comprimento
    return a


print('CALCULE A ÁREA DO SEU TERRENO RETANGULAR: ')
larg = float(input('Digite a largura [m]: '))
comp = float(input('Digite o comprimento [m]: '))
print(f'A área do terreno em questão é de {area(larg, comp):.2f}m.')
