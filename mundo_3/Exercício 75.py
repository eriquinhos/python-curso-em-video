a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite um último número: '))
typed = (a, b, c, d)
print(f'Você digitou os números: {typed}')
print(f'O valor 9 aparece {typed.count(9)} vezes.')
if 3 in typed:
    print(f'O valor 3 apareceu na {typed.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for val in typed:
    if val % 2 == 0:
        print(val, end=' ')
