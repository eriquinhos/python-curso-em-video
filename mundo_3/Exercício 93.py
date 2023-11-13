dados = dict()
dados['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?\nR: '))
dados['Gols'] = list()
dados['Total'] = 0
for i in range(0, partidas):
    dados['Gols'].append(int(input(f'Quantos gols na partida {i+1}: ')))
    dados['Total'] += dados['Gols'][i]
print('-=-' * 30)
print(dados)
print('-=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-=-' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas:')
for k, v in enumerate(dados['Gols']):
    print(f'=> Na partida {k+1}, fez {v} gols;')
print(f'Foi um total de {dados["Total"]} gols.')
