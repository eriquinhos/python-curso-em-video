from datetime import datetime


def vote(year):
    opc = 'Voto Opcional'
    obg = 'Voto Obrigatório'
    n = 'Não vota'
    age = datetime.today().year - int(year)
    if age >= 0:
        if age >= 70 or 16 <= age < 18:
            return age, opc
        elif age < 16:
            return age, n
        else:
            return age, obg
    else:
        return ValueError


try:
    idade = vote(input('Ano de nascimento: '))
    print(f'Com {idade[0]} anos: {idade[1].upper()}')
except ValueError or TypeError:
    print('Valor Inválido')
