#Make a guessing game
import random
from time import sleep
n = random.randint(0, 5)
print('\033[033m', '\033[1m', '-=-'*20)
print('\033[034m', 'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m','-=-'*20)
num = int(input('Em que número eu pensei? '))
print('\033[035m', 'PROCESSANDO...')
sleep(3)
if num == n:
    print('\033[031', 'PARABÉNS! Você acertou!')
else:
    print('\033[031', 'GANHEI! Eu pensei em {}, não em {}!'.format(n, num))