# Escreva um programa de pedra, papel ou tesoura
from time import sleep
from random import randint
print('-=-' * 19)
print('-=-' * 8, 'JOKENPÔ', '-=-' * 8)
print('-=-' * 19)
print('Bem vindo(a)! Você já conhece as regras do jogo?')
print('[ 1 ] SIM')
print('[ 2 ] NÃO')
resposta = int(input('Sua resposta: '))
if resposta == 1:
    print('Então, vamos começar a jogar!')
elif resposta == 2:
    print('No jogo, deve-se escolher pedra, papel ou tesoura. Segue-se os seguintes princípios:')
    print('Pedra ganha da tesoura (amassando-a ou quebrando-a).')
    print('Tesoura ganha do papel (cortando-o).')
    print('Papel ganha da pedra (embrulhando-a).')
else:
    print('Resposta Inválida! Tente novamente.')

print('Você pode escolher entre pedra, papel ou tesoura.')
print('E aí, qual vai ser?')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha = int(input('Sua escolha: '))
computer = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 11)
if escolha == 0:
    if computer == 0:
        print('Computador jogou PEDRA!')
        print('Jogador jogou PEDRA!')
        print('-=' * 11)
        print('EMPATE!!!')
    elif computer == 1:
        print('Computador jogou PAPEL!')
        print('Jogador jogou PEDRA!')
        print('-=' * 11)
        print('COMPUTADOR VENCE!!!')
    else:
        print('Computador jogou TESOURA!')
        print('Jogador jogou PEDRA!')
        print('-=' * 11)
        print('JOGADOR VENCE!!!')
elif escolha == 1:
    if computer == 0:
        print('Computador jogou PEDRA!')
        print('Jogador jogou PAPEL!')
        print('-=' * 11)
        print('JOGADOR VENCE!!!')
    elif computer == 1:
        print('Computador jogou PAPEL!')
        print('Jogador jogou PAPEL!')
        print('-=' * 11)
        print('EMPATE!!!')
    else:
        print('Computador jogou TESOURA!')
        print('Jogador jogou PAPEL!')
        print('-=' * 11)
        print('COMPUTADOR VENCE!!!')
elif escolha == 2:
    if computer == 0:
        print('Computador jogou PEDRA!')
        print('Jogador jogou TESOURA!')
        print('-=' * 11)
        print('COMPUTADOR VENCE!!!')
    elif computer == 1:
        print('Computador jogou PAPEL!')
        print('Jogador jogou TESOURA!')
        print('-=' * 11)
        print('JOGADOR VENCE!!!')
    else:
        print('Computador jogou TESOURA!')
        print('Jogador jogou TESOURA!')
        print('-=' * 11)
        print('EMPATE!!!')
else:
    print('Jogada Inválida!! Tente novamente.')