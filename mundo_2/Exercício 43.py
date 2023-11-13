# Escreva um programa que calcule o IMC de uma pessoa e indique se ela está no peso ideal
alt = float(input('Digite sua altura [m]: '))
peso = float(input('Digite seu peso [kg]: '))
IMC = peso / (alt ** 2)
if IMC < 16:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de MAGREZA GRAVE!')
elif 16 <= IMC < 17:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de MAGREZA MODERADA!')
elif 17 <= IMC < 18.5:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de MAGREZA LEVE!')
elif 18.5 <= IMC < 25:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está SAUDÁVEL!')
elif 25 <= IMC < 30:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de SOBREPESO!')
elif 30 <= IMC < 35:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de OBESIDADE (Grau I)!')
elif 35 <= IMC < 40:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de OBESIDADE SEVERA (Grau II)!')
else:
    print('O IMC dessa pessoa é de {}kg/m²!'.format(IMC))
    print('Ela está em um estado de OBESIDADE MÓRBIDA (Grau III)!')