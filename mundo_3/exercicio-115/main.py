from interface import style
from manager import app
import pandas as pd

df = pd.read_csv('python-curso-em-video/mundo_3/exercicio-115/database/infos.csv', delimiter=',')

print(style.menu_principal('MENU PRINCIPAL'))

while True:
    print(style.opcoes_do_usuario('1 - Ver pessoas cadastradas\n'
    '2 - Cadastrar nova pessoa\n3 - Sair do sistema'))

    try:
        opcao = int(input(style.escolha('Sua opção: ')))

        if opcao == 1:
            print(style.pessoas_cadastradas(app.ver_pessoas_cadastradas(df)))
        elif opcao == 2:
            df = app.cadastra_usuario(input('Nome: '), int(input('Idade: ')), df)
        elif opcao == 3:
            break
        else:
            print(style.erro_opcao('ERRO! Digite uma opção válida!'))

    except TypeError or ValueError:
        print(style.erro_opcao('ERRO! Digite uma opção válida!'))

    except KeyboardInterrupt or EOFError:
        print(style.erro_opcao('O usuário preferiu não informar os dados!'))
        break

 