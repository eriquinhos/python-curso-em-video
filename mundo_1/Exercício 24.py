# Make a program to show if the city begins with "Santo"

city = str(input('What city have you borned? ')).strip()
print(city[:5].upper() == 'SANTO')
