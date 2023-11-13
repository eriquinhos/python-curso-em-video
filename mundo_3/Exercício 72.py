extenso =('zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze',
          'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf', 'vingt' )
num = int(input('Digite um número de 0 a 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente. Digite um número de 0 a 20: '))

print(f'O numero digitado foi {extenso[num]}.')
