chamada = list()
info = list()
while True:
    info.append(str(input('Nome: ')).strip().capitalize())
    info.append(float(input('Nota 1: ')))
    info.append(float(input('Nota 2: ')))
    chamada.append(info.copy())
    info.clear()
    cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=-' * 30)
print('{:^5}{:^10}{:^10}'.format('Nº', 'Nome', 'Média'))
print('-' * 30)
for i, v in enumerate(chamada):
    print(f'{i:^5}{v[0]:^10}{(v[1]+v[2])/2:^10}')
print('-' * 30)
who = 0
while True:
    who = int(input('Deseja ver as notas de qual aluno [999 interrompe]: '))
    if who == 999:
        print('Obrigado por usar nosso programa!')
        break
    for i, v in enumerate(chamada):
        if i == who:
            print(f'As notas de {chamada[who][0]} são {chamada[who][1]:.1f} e {chamada[who][2]:.1f}.')