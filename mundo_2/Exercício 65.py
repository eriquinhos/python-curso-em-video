quant = 0
soma = 0
major = 0
minor = 0
resp = 'S'
while resp == 'S':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        major = num
        minor = num
    else:
        if num > major:
            major = num
        else:
            minor = num
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
print(f'Você digitou {quant} números e a média entre eles foi de {soma/quant}.')
print(f'O maior entre eles foi {major} e o menor foi {minor}.')