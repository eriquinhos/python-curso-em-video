from random import randint
numeros = []
tot = 1
jogos = []
print('-=-' * 10)
print('{:^30}'.format('MEGA SENA'))
print('-=-' * 10)
plays = int(input('Digite quantos jogos você deseja gerar: '))
while plays >= tot:
    quant = 0
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            quant += 1
        if quant >= 6:
            break
    numeros.sort()
    jogos.append(numeros.copy())
    numeros.clear()
    tot += 1
for c in range(0, plays):
    print(f'Jogo {c+1}: {jogos[c]}')
