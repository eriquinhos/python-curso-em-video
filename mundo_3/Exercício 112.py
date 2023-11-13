from modules import moeda
from modules.dado import leia_dinheiro

p = leia_dinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
