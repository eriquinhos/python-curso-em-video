# Write a program to ask 7 int numbers and show the sum of the even numbers only
soma = 0
for c in range(0, 6):
    num = int(input('Type a number: '))
    if num % 2 == 0:
        soma += num
print('The sum of the even numbers is: {}.'.format(soma))
