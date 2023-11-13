#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#  A média de idade do grupo
#  Qual o nome do HOMEM mais velho
#  Quantas mulheres tem menos de 20 anos
nome = []
idade = []
sexo = []
soma_Idades = 0
velho_Nome = ""
velho_Idade = 0
mulheres = 0
for c in range(0, 4):
    print(f'==== {c+1}ª PESSOA ====')
    nome.append(str(input('Nome: ')).strip())
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo: ').strip().upper()))
    if c == 0 and sexo[0] == "M":
        velho_Nome = nome[0]
        velho_Idade = idade[0]
    else:
        if idade[c] > velho_Idade and sexo[c] == "M":
            velho_Nome = nome[c]
            velho_Idade = idade[c]
    if sexo[c] == "F" and idade[c] < 20:
        mulheres += 1
    soma_Idades += idade[c]
media = soma_Idades/4
print(f'A média de idade do grupo é de {media:.2f} anos.')
print(f'O homem mais velho tem {velho_Idade} anos e chama-se {velho_Nome}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
