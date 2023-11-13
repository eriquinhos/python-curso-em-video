# Create a program that has the function readInt(). It is going to work as an input(), but validating the value,
# accepting only numbers (Ex: n = readInt('Type a number: ')

def readint(string):  # Define the readint() function
    valid = False  # The typed value is not valid yet
    value = 0  # The standard value is 0
    while True:  # An infinite loop is created
        num = str(input(string))  # The user should type a number when asked
        if num.isnumeric():  # If the value is truly numeric, it will happen:
            value = int(num)
            valid = True  # Now it has a valid value
        else:
            print('ERROR, TYPE A VALID NUMBER!')  # If the value is not valid, this message will appear on the screen
        if valid:  # And if the value is valid, the loop will end
            break
    return value  # The function will return this value


n = readint('Type a Number: ')
print(f'You typed the number {n}.')
