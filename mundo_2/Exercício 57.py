#  Faça um programa que leia o sexo de uma pessoa mas só aceita 'M' ou 'F'. Caso esteja errado, peça
#  a digitação correta até ter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')
