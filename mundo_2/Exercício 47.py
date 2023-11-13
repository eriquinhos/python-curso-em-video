# Write a program to show all the even numbers between two numbers and the sum
begin = int(input('Type the beginning of the interval: '))
end = int(input('Type the end of the interval: '))
som = 0
for a in range(begin, end + 1):
    if a % 2 == 0:
        print(a, end=' ')
        som += a
print('\n')
print("The sum of the pairs in this interval is {}".format(som))
