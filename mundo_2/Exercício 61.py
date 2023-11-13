#  Refaça o exercício 051 usabdo while
an = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
termos = 10
while termos > 0:
    print(f'{an} ⇀ ', end='')
    an  += r
    termos -= 1
print('FIM')
