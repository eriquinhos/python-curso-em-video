# Make a program to calculate the price of a product with discount
def isnumber(string):  # This function will define if the typed value is numeric, since the isnumeric() function does
    # not consider a "float type string" as a number. So we must create our own function for it.
    try:
        float(string)  # This function will try convert the string in a float type.
        return True
    except ValueError:
        return False  # Return true if it is successful, False if it is not


valid = False  # At this moment, any value is valid
while True:  # So, we create this loop
    price = str(input('How much is this product? R$'))  # In both inputs the user should type a number (int/float)
    discount = str(input('Whats the discount rate [%]? '))
    if isnumber(price) and isnumber(discount):  # If both values are numbers, so they are valid values
        price = float(price)
        discount = float(discount)
        valid = True
    else:  # If it is not, the loop will go back to the inputs
        print('One of the typed values is invalid. Try again.')
    if valid:  # But if both values are valid, the loop ends
        break
print('If the product costs R${:.2f} and the discount rate is {}%, so now it costs R${:.2f}!'.format(price, discount,
                                                                                                     price * (1 -
                                                                                                              (discount
                                                                                                               / 100))))
