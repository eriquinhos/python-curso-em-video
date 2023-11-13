from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
for c in range(0,4):
    jogo[f"Jogador {c+1}"] = randint(1, 6)
print(f'{"Valores Sorteados:":-^30}')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-=-' * 10)
print(f'{"RANKING DOS JOGADORES:":^30}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c in range(0, 4):
    print(f'{c+1}º Lugar: {ranking[c][0]} com {ranking[c][1]};')
    sleep(1)
