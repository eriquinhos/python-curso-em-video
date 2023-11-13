print("GERADOR DE PROGRESSÕES ARITMÉTICAS")
print("-="*17)
a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da PA: "))
termos = 0
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{a1} ⇒ ', end='')
        a1 += r
        contador += 1
        termos += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos mais você gostaria de ver: '))
print(f'Progressão aritmérica finalizada com {termos} termos mostrados.')