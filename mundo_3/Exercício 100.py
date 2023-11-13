from random import randint
from time import sleep

def randlist():
    l = list()
    for i in range(0,5):
        l.append(randint(0, 20))
    return l

def sumpair(var):
    sum = 0
    for j in var:
        if j % 2 == 0:
           sum += j
    return sum


lis = randlist()
print('Uma lista aleatória com 5 números: ', end='')
for val in lis:
    print(val, end=' ')
    sleep(0.5)
print(f'\nSomando os pares da lista, temos: {sumpair(lis)}.')