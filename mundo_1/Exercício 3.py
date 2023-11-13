# Make a program that shows you the sum of two numbers.

try:
    number_1 = float((input('Type a number: ')))  # It receives a random number
    number_2 = float((input('Type another number: ')))  # It receives another random number

    sumNumbers = number_1 + number_2  # The program is going to try add these two numbers
    print('The sum of {} and {} equals to {}'.format(number_1, number_2, sumNumbers))  # If it is successful, it will
                                                                                        # print the sum
except ValueError:
    print('The program could not recognize the typed information. Please, try again.')
