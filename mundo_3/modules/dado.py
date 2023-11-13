def leia_dinheiro(msg):
    while True:
        valor = str(input(msg)).strip().replace(',', '.')
        try:
            float(valor)
            return float(valor)
        except:
            print(f'\033[31mERRO: \"{valor}\" é um preço inválido!\033[m')