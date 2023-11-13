# Write a program to calculate a salary increase
#If salary > 1250, increase = 10%
#If salary <= 1250, increase = 15%
salary = float(input("What's your salary? R$"))
if salary > 1250:
    increase = 10
    print('The new salary is R${:.2f}!'.format(salary * (1 + increase/100)))
else:
    increase = 15
    print('The new salary is R${:.2f}'.format(salary * (1 + increase/100)))
