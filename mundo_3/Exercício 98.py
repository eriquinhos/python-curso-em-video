from time import sleep


def sequence(start, stop, step=1):
    """
    :param start: START sequence
    :param stop: STOP sequence
    :param step: pace of the sequence
    :return: sequence of numbers
    """
    lista = list()
    try:
        if start and stop:
            while start <= stop:
                lista.append(start)
                start += step
            for j in lista:
                print(j, end=' ')
                sleep(0.5)
        else:
            while start >= stop:
                lista.append(start)
                start += step
            for j in lista:
                print(j, end=' ')
                sleep(0.5)
        print()
    except:
        return


sequence(1, 10)
sequence(10, 0, -2)
print("Now it's your turn:")
a = input('Start: ')
b = input('End: ')
c = input('Pace: ')
try:
    a = int(a)
    b = int(b)
    c = int(c)
    sequence(a, b, c)
except:
    print('Invalid Values.')
