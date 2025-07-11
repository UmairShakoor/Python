# This Program Converts user's data to different Cases

data = input('\nEnter a sentence/word to convert into different Cases: ')

print(f'\nLowerCase: {data.lower()}') # LowerCase (All Characters UnCapital)
print(f'UpperCase: {data.upper()}') # UpperCase (All Characters Capital)
print(f'\nCapital: {data.capitalize()}') # Capitalized (First Character of First Word Capital)
print(f'Title: {data.title()}\n') # Titled (First Character of all Words Capital))
