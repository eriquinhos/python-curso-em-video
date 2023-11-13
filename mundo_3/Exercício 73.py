english_Football = ('Manchester City', 'Manchester United', 'Leicester', 'Chelsea', 'West Ham', 'Tottenham',
                    'Liverpool', 'Everton', 'Arsenal', 'Aston Villa', 'Leeds United', 'Crystal Palace', 'Wolverhampton',
                    'Southampton', 'Burnley', 'Brighton', 'Newcastle', 'Fulham', 'West Bromwich', 'Sheffield United')
print('-=-' * 40)
print(f'Teams List:')
for pos, team in enumerate(english_Football):
    print(f'{pos+1}º: {team}')
print('-=-' * 40)
print('Top Five:')
for i in range(0, 5):
    print(f'{i+1}º: {english_Football[i]}')
print('-=-' * 40)
print('Bottom Five:')
for i in range(19, 14, -1):
    print(f'{i+1}º: {english_Football[i]}')
print('-=-' * 40)
print('Alphabetic Order:')
for i in range(0, len(english_Football)):
    print(f'{sorted(english_Football)[i]}')
print('-=-' * 40)
print(f'Liverpool is in the {english_Football.index("Liverpool")+1}º position.')
