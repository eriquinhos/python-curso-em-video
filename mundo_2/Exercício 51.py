# Write a program to ask the first  term and the common difference of a arithmetic progression
print('=' * 40, '\n', 'ARITHMETIC PROGRESSION CALCULATOR', '\n', '=' * 39)
fT = int(input('First Term: '))
cD = int(input('Common Difference: '))
terms = fT + (int(input('Number of terms: ')) - 1) * cD
for c in range(fT, terms + cD, cD):
    print(c, end=' → ')
print('ACABOU!')
