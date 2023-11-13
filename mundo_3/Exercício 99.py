def bigger(var):
    major = 0
    for pos, val in enumerate(var):
        if pos == 0:
            major = val
        else:
            if val > major:
                major = val
    return major


a = []
while True:
    item = input('Digite um valor inteiro: ')
    try:
        int(item)
        a.append(item)
    except ValueError:
        None
    cont = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if cont == 'N':
        break
print('Você digitou os seguintes valores: ', end='')
for values in a:
    print(values, end=' ')
print()
print(f'Você digitou {len(a)} valores.')
print(f'O maior valor digitado foi {bigger(a)}.')
