while True:
    mult = int(input('Digite um número para ver a tabuada: '))
    if mult > 0:
        for c in range(1, 11):
            print(f'{mult} x {c:2} = {mult*c}')
    else:
        print('PROGRAMA TABUADA ENCERRADO! Volte sempre!')
        break
