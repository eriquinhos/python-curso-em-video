# Draw lots 4 students to erase a board
import random
st1 = str(input("Write a student's name: "))
st2 = str(input("Write a student's name: "))
st3 = str(input("Write a student's name: "))
st4 = str(input("Write a student's name: "))
lists = [st4, st3, st2, st1]

print("{} will erase the board!".format(random.choice(lists)))