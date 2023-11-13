# Write a program that can tell if a year is leap or not
from datetime import date
year = int(input('What year do you want to analyse? (Type 0 to this year) '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{} is a LEAP YEAR".format(year))
else:
    print("{} is NOT A LEAP YEAR".format(year))
