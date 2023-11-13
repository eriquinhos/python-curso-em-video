num = 0
cont = 0
soma = 0
while num != -1:
    num = int(input('Digite um número [-1 para parar]: '))
    if num != -1:
        soma += num
        cont += 1
    else:
        print('FIM')
print(f'Programa finalizado. Você digitou {cont} números e a soma entre eles foi {soma}.')
