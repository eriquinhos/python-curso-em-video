'''# Matriz 3 x 3
linha_1 = [[],[],[]]
linha_2 = [[],[],[]]
linha_3 = [[],[],[]]
for i in range(0, 3):
    linha_1[i].append(int(input(f'Digite o elemento a1{i+1}: ')))
for i in range(0, 3):
    linha_2[i].append(int(input(f'Digite o elemento a2{i+1}: ')))
for i in range(0, 3):
    linha_3[i].append(int(input(f'Digite o elemento a3{i+1}: ')))
for j in linha_1:
    print(j, end=' ')
print()
for j in linha_2:
    print(j, end=' ')
print()
for j in linha_3:
    print(j, end=' ')'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for m in range(0, 3):
    for n in range(0, 3):
        matriz[n][m] = int(input(f'Digite o valor do a{m+1}{n+1}: '))
for m in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[m][n]:^5}]', end=' ')
    print()
