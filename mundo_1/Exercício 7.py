# Make a program that calculates the average grade of a student
try:   # The program will try running
    grade_1 = float(input("Type the first grade: "))  # The user should type a int/float type value here
    grade_2 = float(input("Type the second grade: "))  # The user should type a int/float type value here

    print('The average grade of this student is {:.2f}'.format((grade_1 + grade_2) / 2))
    # It will print the student's average grade

except ValueError:  # If the user does not type a valid value, this message will appear on its screen
    print('Invalid Value. Please, try again.')
