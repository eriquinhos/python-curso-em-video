def ajuda(com):
    help(com)

if __name__ == '__main__':
    print('\033[1;36m-'*30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('-'*30)
    print('\033[m')

    while True:
        comando = str(input('\033[1;32mFunção ou Biblioteca > \033[m')).strip().lower()
        if comando == 'FIM':
            break
        else:
            try:
                ajuda(comando)
            except TypeError:
                print('\033[1;31mERRO! Por favor, digite um comando válido.\033[m')