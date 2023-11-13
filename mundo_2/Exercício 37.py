# Escreva um programa que faça a conversão de decimais para BINÁRIO, OCTAL ou HEXADECIMAL
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
choice = int(input('Sua escolha: '))
if choice == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif choice == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif choice == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

