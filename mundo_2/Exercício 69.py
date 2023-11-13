idade = mais18 = homem = m_Menos20 = 0
sexo = cont = ''
while True:
    print('---' * 20)
    print('CADASTRE UMA PESSOA')
    print('---' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    elif sexo == 'M':
        homem += 1
    elif idade < 20 and sexo == 'F':
        m_Menos20 += 1
    print('---' * 20)
    cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}.')
print(f'Total de homens cadastrados: {homem}.')
print(f'Total de mulheres com menos de 20 anos: {m_Menos20}.')
