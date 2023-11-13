#  Crie um programa que leia 2 valores e mostre um menu e seu programa deve realizar a operação
#  solicitada em cada caso
from time import sleep
n1= int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
choice = 0
while choice != 5:
    print('Operações a serem realizadas:')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair')
    choice = int(input('Sua escolha: '))
    if choice == 1:
        print(f'O resultado de {n1} + {n2} é {n1+n2}.')
        sleep(2)
    elif choice == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}.')
        sleep(2)
    elif choice == 3:
        if n1 > n2:
            print(f'O maior número entre esses é {n1}.')
        elif n1 < n2:
            print(f'O maior número entre esses é {n2}.')
        else:
            print('Os dois números são iguais!')
        sleep(2)
    elif choice == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif choice > 5 or choice < 1:
        print('Opção Inválida! Tente novamente!')
print('Finalizando...')
sleep(2)
print('Fim do Programa! Volte Sempre!')