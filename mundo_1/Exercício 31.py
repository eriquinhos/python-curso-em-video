# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da
# passagem cobrando 0,50 por Km rodado para viagens até 200Km e 0,45 para viagens mais longas.

km = float(input('Digite a distância que deseja percorrer [km]: '))
if km > 200:
    print('A passagem ficará em R${:.2f}!'.format(km * 0.45))
else:
    print('A passagem ficará em R${:.2f}!'.format(km * 0.50))