# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma
# mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando 7 reais por Km
# acima de 80km/h.

speed = float(input('Digite a velocidade: '))
value = (speed - 80) * 7
if speed > 80:
    print('Você foi multado! Favor pagar o valor de R${:.2f}.'.format(value))
else:
    print('Continue a dirigir com segurança!')