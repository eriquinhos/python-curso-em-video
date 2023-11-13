dados = {'Nome': [], 'Gols': [], 'Total': []}
pos = 0
while True:
    dados['Nome'].append(str(input('Nome do Jogador: ')).strip().capitalize())
    partidas = int(input(f'Quantas partidas {dados["Nome"][pos]} jogou?\nR: '))
    gols = []
    total = 0
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
    total = sum(gols.copy())
    dados['Total'] = total
    dados['Gols'].append(gols.copy())
    cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    pos += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=-' * 30)
print('{:^5}{:^10}'.format('COD', 'Nome'))
print('-' * 15)
for i, j in enumerate(dados['Nome']):
    h = str(i)
    print(f'{h:^5}{j:^10}')
while True:
    who = int(input('Mostrar dados de qual jogador [999 interrompe]: '))
    if who == 999:
        print('Obrigado por usar nosso programa!')
        break
    for i, v in enumerate(dados['Gols']):
        if who == i:
            print(f'LEVANTAMENTO DO JOGADOR {dados["Nome"][who]}')
            for j, k in enumerate(dados['Gols'][who]):
               print(f'No jogo {j + 1} fez {k} gols')
            print(f'Total de gols: {dados["Total"][who]}')
print('<< ENCERRADO >>')