def fact(var, show=True):
    """
    Caulculates a number's factorial
    :param var: choose a number to calculate its factorial
    :param show: True for showing the process
    :return: Factorial
    """
    list = []
    factorial = 1
    var = int(var)
    if show:
        while var > 0:
            list.append(var)
            factorial *= var
            var -= 1
        return factorial
    else:
         while var > 0:
            factorial *= var
            var -= 1
    return factorial


num = input('Digite um valor inteiro para calcular o fatorial: ')
want = str(input('Deseja ver o processo? [S/N] ')).upper()[0]
try:
    num = int(num)
    if want == 'S':
        print(f'O fatorial de {num} é calculado por {fact(num)}.')
    elif want == 'N':
        print(f'O fatorial de {num} é {fact(num, False)}.')
except ValueError or TypeError:
    print('Valor Inválido')
