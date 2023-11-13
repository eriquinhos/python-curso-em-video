def escreva(mensagem):
    """
    Printa uma mensagem de tamanho adptável
    :param mensagem: A mensagem que você deseja escrever
    :param caracteres: Número de caracteres da mensagem
    :return: None
    """
    if type(mensagem) == str:
        caracteres = len(mensagem) + 4
        print('~'*caracteres)
        print(f'  {mensagem}')
        print('~'*caracteres)
    else:
        return


msg = str(input('Escreva uma mensagem: '))
escreva(msg)
