import pandas as pd
from interface import style


def cadastra_usuario(nome, idade, arquivo=pd.read_csv('python-curso-em-video/mundo_3/exercicio-115/database/infos.csv')):
    try:
        arquivo.loc[len(arquivo)] = [nome, idade]

        arquivo.sort_values(['Nome'], ascending=True)

        return arquivo.to_csv(arquivo, index=False)

    except FileNotFoundError:
        print(style.erro_opcao('O arquivo não foi encontrado!'))


@style.pessoas_cadastradas
def ver_pessoas_cadastradas(arquivo=pd.read_csv('python-curso-em-video/mundo_3/exercicio-115/database/infos.csv')):
    try:
        for index, row in arquivo.iterrows():
            print(f'{row["Nome"]:<30} {row["Idade"]:^10} anos')

    except FileNotFoundError:
        print(style.erro_opcao('O arquivo não foi encontrado!'))

    except pd.errors.EmptyDataError:
        print(style.erro_opcao('Não há pessoas cadastradas no sistema!'))
