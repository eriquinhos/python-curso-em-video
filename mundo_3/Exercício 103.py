# Make a program which has a function that receives optional parameters: The player's name and The amount of goals
# in the match. The program should be able to show data without error, even though the user do not type any valid value

def match(player='<unknown>', goals=0):  # First, we have to define a function called match
    print(f'The player named {player} scored {goals} goals.')  # It will just print this message


print('-' * 20)
name = str(input("Player's name: "))  # The user should type or not a name
score = str(input('Goals: '))  # The user should type or not an int type value
if score.isnumeric():   # If the string is a numeric string, so we can turn it into an int type
    score = int(score)
else:  # But if it is not, the program will not consider as a valid value and is going to consider the score as 0
    score = 0
if name.strip() == '':  # If the typed name is empty, the function will only receive the goals value
    match(goals=score)
elif name.isnumeric():  # If the typed name is a number, the function will only receive the goals value
    match(goals=score)
else:  # But if it is not, we will have both the values defined
    match(name, score)
print('-' * 20)
