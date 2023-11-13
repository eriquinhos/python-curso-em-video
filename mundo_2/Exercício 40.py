# Write a program to calculate the average grade
# If avg < 5: reproved
# If avg >= 7: approved
grade_1 = float(input("Type your grade: "))
grade_2 = float(input("Type your another grade: "))
avg = (grade_1 + grade_2)/2
if avg < 5:
    print('If the grades are {} and {}, the average is {}!'.format(grade_1, grade_2, avg))
    print('The student is REPROVED!')
elif avg >= 7:
    print('If the grades are {} and {}, the average is {}!'.format(grade_1, grade_2, avg))
    print('The student is APPROVED!')
else:
    print('If the grades are {} and {}, the average is {}!'.format(grade_1, grade_2, avg))
    print('The student is RECOVERING!')
