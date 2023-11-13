'''Nant = 1
Fibonacci = 0

n = int(input('Nº de elementos da sequência: '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1'''
quant = int(input("Digite o número de elementos a ser mostrado: "))
st_Term = 0
nd_Term = 1
print (f'{st_Term} ⇀ {nd_Term} ⇀ ', end='')
cont = 3
while cont <= quant:
    next_Term = st_Term + nd_Term
    print(f'{next_Term} ⇀ ', end='')
    st_Term = nd_Term
    nd_Term = next_Term
    cont += 1
print('FIM')
