# Make a program to calculate the new salary of a employee after a increase
def isnumber(string):  # This function will define if the typed value is numeric, since the isnumeric() function does
    # not consider a "float type string" as a number. So we must create our own function for it.
    try:
        float(string)  # This function will try convert the string in a float type.
        return True
    except ValueError:
        return False  # Return true if it is successful, False if it is not


valid = False  # The typed value is not valid yet, because it's None
while True:
    salary = input('How much is the salary? R$')  # In both variables the user should type a int/float value
    increase = input('Whats the increase rate [%]? ')  # And here, the user should use a percent value. Ej: 50%
    if isnumber(salary) and isnumber(increase):
        salary = float(salary)  # If both typed values are numbers, sou we're gonna convert it to float
        increase = float(increase)
        valid = True
    else:  # If it's not, the following message will appear and the user will have to type the values again
        print('You typed a invalid value. Please, try again!')
    if valid:  # But if it's valid, the loop will end
        break

print('If the salary is R${:.2f} and the increase rate is {}%, so the new salary is R${:.2f}!'.format(salary, increase,
                                                                                                      salary *
                                                                                                      (1 + (increase
                                                                                                            / 100))))
# In the end, it will print the new salary
