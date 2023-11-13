def define_cor(cor):
    cores = {
        'vermelho': '\033[1;31m',
        'verde': '\033[1;32m',
        'azul': '\033[1;34m',
        'amarelo': '\033[1;33m',
        'roxo': '\033[1;35m',
        'ciano': '\033[1;36m',
        'cinza': '\033[1;37m',
        'limpa': '\033[m'
    }

    def colore_texto(func):

        def wrapper(*args, **kwargs):
            return cores[cor]+func(*args, **kwargs)+cores['limpa']
        return wrapper
    return colore_texto


def pessoas_cadastradas(func):
    def tabela_das_pessoas(*args, **kwargs):
        print('-'*40)
        print(f'{"PESSOAS CADASTRADAS":^40}')
        print('-'*40)
        func(*args, **kwargs)
        print('-'*40)
    return tabela_das_pessoas


@define_cor('ciano')
def menu_principal(texto):
    return '-'*40+f'\n{texto:^40}\n'+'-'*40


@define_cor('azul')
def opcoes_do_usuario(texto):
    return f'{texto}'


@define_cor('ciano')
def escolha(texto):
    return '-' * 40 + f'\n{texto}'


@define_cor('vermelho')
def erro_opcao(texto):
    return '\n'+'-'*40+f'\n{texto:^40}\n'+'-'*40
