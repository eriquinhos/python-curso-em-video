#  Melhore o jogo do DESAFIO 028 em que o computador vai "pensar" em um número entre 0 e 10
#  O jogador vai tentar adivinhar até acertar e no final mostrará o número de tentativas
from random import randint
numeroAleatorio = randint(0,10)
tentativas = 1
print('\033[033m', '\033[1m', '-=-'*20)
print('\033[034m', 'Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('\033[33m','-=-'*20)
escolha = int(input('\n\033[;93mEscolha um número: '))
while escolha != numeroAleatorio:
    print('\033[;91m', 'Poxa, não foi dessa vez!')
    if escolha < numeroAleatorio:
        escolha = int(input('Tente um número maior: '))
    else:
        escolha = int(input('Tente um número menor: '))
    tentativas += 1
print(f'\n\033[1;36mParabéns! Acertou com {tentativas} tentativas.')
