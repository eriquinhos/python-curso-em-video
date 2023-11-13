# Write a program to sum the odd numbers and multiple of 3
begin = int(input('Type the beginning of the interval: '))
end = int(input('Type the end of the interval: '))
som = 0
cont = 0
for a in range(begin, end + 1):
    if a % 3 == 0 and a % 2 != 0:
        print(a, end=' ')
        som += a
        cont += 1
print('\n')
print('The sum of the {} odd numbers, multiples of 3, between {} and {} is {}.'.format(cont, begin,
                                                                                       end, som))