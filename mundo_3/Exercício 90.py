dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 6.0:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k}: {v}')
