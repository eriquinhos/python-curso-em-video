import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    print('\033[0;32m'
          'Consegui acessar o site Pudim com sucesso!'
          '\033[m')
except urllib.error.URLError:
    print('\033]0;31m'
          'O site Pudim não está acessível no momento.'
          '\033[m')