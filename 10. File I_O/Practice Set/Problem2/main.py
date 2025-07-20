'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
'''

import random

def game():
    score = random.randint(1, 62) # Stores random number b/w 1 & 62
    
    print('You are playing the game...')
    print(f'\nYour Score: {score}\n')
    
    return str(score)

score = game() # Starts game & Stores Score

with open('Hi-Score.txt', 'w+') as f:
    if f.read() == '':
        f.write('0\n')
        
    high_score = f.read().replace(' ','')

if score > high_score:
    with open('Hi-Score.txt', 'w') as f:
        f.write(f'{score}\n')
