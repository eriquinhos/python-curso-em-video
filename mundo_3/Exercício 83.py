lista = list(str(input('Digite uma expressão: ')))
abre = []
fecha = []
for v in lista:
    if v == '(':
        abre.append(v)
    if v == ')':
        fecha.append(v)
if len(abre) == len(fecha):
    print('A expressão digitada é válida!')
else:
    print('A expressão digitadda é inválida!')
