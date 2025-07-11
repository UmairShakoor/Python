# Snake, Water & Gun game using Python !!

import random
from colorama import Fore, Style, init # For colored UI in terminal

init(autoreset=True) # Initialize colorama for Windows compatibility

computer = random.choice([1, -1, 0]) # Randomly choose number for the list

# Project Name
print(Fore.WHITE +'\n=========================')
print(Fore.BLUE + Style.BRIGHT + '\tSWG Game')
print(Fore.WHITE + '=========================')


# Input Validation
while True: # Infinite Loop
    you_str = input(Fore.BLUE + Style.BRIGHT + '\nEnter your choice (s,w,g): ') # Input
    you_str = you_str.replace(' ','') # Removes spaces

    if you_str.isdigit(): # if you_str contains a digit
        print(Fore.RED + 'Input Invalid, it can\'t be a number')
        continue

    you_str = you_str.lower() # Convertion to lowerCase to avoid case-issue

    if not(('s' == you_str) or ('w' == you_str) or ('g' == you_str)): # if you_str not(equal to) s,w or g
        print(Fore.RED + 'Input must be s (snake), w (water) or g (gun)')
        continue

    break
# Input Validated

youDict = {'s': 1, 'w': -1, 'g': 0}
you = youDict[you_str] # Stores number(1,0,-1) from youDict

reverseDict = {1: 'Snake', -1: 'Water', 0: 'Gun'}
print(Fore.GREEN + f'\nYou chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}\n')

# Draw
if computer == you:
    print(Fore.YELLOW + Style.BRIGHT + '\tIt is a draw!\n')

else:
    # 1(Snake) Possibilities
    if computer == 1 and you == -1:
        print(Fore.RED + '\tYou Lose!\n')

    elif computer == 1 and you == 0:
        print(Fore.WHITE + Style.BRIGHT + '\tYou Win!\n')

    # -1(Water) Possibilities
    elif computer == -1 and you == 1:
        print(Fore.WHITE + Style.BRIGHT + '\tYou Win!\n')

    elif computer == -1 and you == 0:
        print(Fore.RED + '\tYou Lose!\n')

    # 0(Gun) Possibilities
    elif computer == 0 and you == 1:
        print(Fore.RED + '\tYou Lose!\n')

    elif computer == 0 and you == -1:
        print(Fore.WHITE + Style.BRIGHT + '\tYou Win!\n')

    # Nothing Works then
    else:
        print(Fore.RED + '\tSomething went wrong!\n')
