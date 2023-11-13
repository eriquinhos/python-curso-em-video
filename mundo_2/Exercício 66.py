num = soma = quant = 0
while True:
    num = int(input('Digite um número [0 STOP]: '))
    if num == 0:
        break
    soma += num
    quant += 1
print(f'Programa finalizado! Você digitou {quant} números e a soma deles foi de {soma}.')