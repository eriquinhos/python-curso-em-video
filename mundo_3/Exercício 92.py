from datetime import datetime
dados = dict()
dados["Nome"] = str(input('Nome: ')).strip().capitalize()
dados["Idade"] = datetime.today().year - int(input('Anos de Nascimento: '))
dados["CTPS"] = int(input('Carteira de Trabalho [0 se não possui]: '))
if dados["CTPS"] != 0:
    dados['Ano de Contratação'] = int(input("Ano de Contratação: "))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados["Idade"] + 35
for k, v in dados.items():
    if k == 'Salário':
        print(f'{k}: R${v:.2f}')
    elif k == 'Aposentadoria':
        print(f'Se aposentará com {v} anos')
    else:
        print(f'{k}: {v}')
