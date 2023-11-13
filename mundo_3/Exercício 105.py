def notas(*args, sit=False):
    '''
    Função para analisar notas (maximo, mínimo e média) e situações de vários alunos.
    :param args: notas dos alunos
    :param sit: situação da turma
    :return: dicionário com as informações
    '''

    # Variáveis
    dicionario = dict()

    dicionario['total'] = len(args)
    dicionario['menor'] = max(args)
    dicionario['maior'] = min(args)
    dicionario['media'] = sum(args) / len(args)

    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'

    return dicionario


# Programa Principal
if __name__ == '__main__':
    resp = notas(5.5, 2.5, 1.5, sit=True)
    print(resp)
    help(notas)
