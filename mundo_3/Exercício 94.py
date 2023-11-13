dados = dict()
dados['Nome'] = list()
dados['Sexo'] = list()
dados['Idade'] = list()
while True:
    dados['Nome'].append(str(input('Nome: ')).strip().capitalize())
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['Sexo'].append(sexo)
    dados['Idade'].append(int(input('Idade: ')))
    cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=-' * 30)
print(f'A) Ao todo temos {len(dados["Nome"])} pessoas cadastradas;')
media = sum(dados["Idade"].copy())/len(dados["Idade"])
print(f'B) A média das idades é de {media:.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for n, v in enumerate(dados['Sexo']):
    if v == 'F':
        print(f'{dados["Nome"][n]}', end=' ')
print()
print('D) Lista de pessoas acima da idade média:')
for i, j in enumerate(dados['Idade']):
    if j > media:
        for k, v in dados.items():
            print(f'    {k}: {v[i]}', end='; ')
        print()
print('<< ENCERRADO >>')
