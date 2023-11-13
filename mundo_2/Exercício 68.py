from random import randint
print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-=-' * 20)
computador = 101
soma = 0
vitorias = 0
while True:
    computador = randint(0, 100)
    jogador = int(input('Digite um valor: '))
    par_Impar = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    soma = computador+jogador
    print('---' * 20)
    if soma % 2  == 0 and par_Impar == 'P':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} DEU PAR!')
        vitorias += 1
        print('---' * 20)
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-' * 20)
    elif soma % 2  == 1 and par_Impar == 'I':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} DEU ÍMPAR!')
        vitorias += 1
        print('---' * 20)
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-' * 20)
    elif soma % 2 == 0 and par_Impar == 'I':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} DEU PAR!')
        print('---' * 20)
        print('VOCÊ PERDEU!')
        print('-=-' * 20)
        break
    elif soma % 2 == 1 and par_Impar == 'P':
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} DEU ÍMPAR!')
        print('---' * 20)
        print('VOCÊ PERDEU!')
        print('-=-' * 20)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')
