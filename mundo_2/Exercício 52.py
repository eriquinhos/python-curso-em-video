n = int(input('Digite um número: '))
div = 0
for a in range(1, n + 1):
    if n % a == 0:
        div += 1
if div == 2:
    print('O número é primo!')
else:
    print('O número NÃO é primo!')