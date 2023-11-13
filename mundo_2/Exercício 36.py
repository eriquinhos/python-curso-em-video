# Write a program to approve a bank loan to buy a house
# It must ask the house's value, the salary of the owner and for how many years he's planning to pay
# The installment can't exceed 30% of the salary
value = float(input("What's the house's value? "))
salary = float(input("How much do you earn per month? "))
time = int(input('How many years do you plan pay it? '))
installment = value / (time*12)
if salary * 0.3 >= installment:
    print('To buy a R${:.2f} house in {} years, the installment is R${:.2f}'.format(value, time,
                                                                                    installment))
    print("The loan CAN be done")
else:
    print('To buy a R${:.2f} house in {} years, the installment is R${:.2f}'.format(value, time, installment))
    print("The loan CAN'T be done")
