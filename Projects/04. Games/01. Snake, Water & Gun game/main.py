# Snake, Water & Gun game using Python !!

import random
import os

print('\n\tSWG Game')

def game(score):
    while True: # Infinite Loop
        you_str = (input('\nEnter your choice (s,w,g): ').replace(' ','')).lower() # Removes spaces and lower case Convertion
   
        if not(you_str in ['s', 'w', 'g']): # if you_str not(equal to) s,w or g
            print('Input must be s (snake), w (water) or g (gun)')
            continue
   
        break
   
   # Input Validated
   
    comp_str = ''.join(random.choices(['s', 'w', 'g'])) # Convert (Randomly choose s, g or w) to string
   
    dict = {'s': 1, 'w': -1, 'g': 0}
    you = dict[you_str] # Stores number(1,0,-1) from dict
    computer = dict[comp_str]
   
    reverseDict = {1: 'Snake', -1: 'Water', 0: 'Gun'}
    print(f'\nYou chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}\n')
      
   # Draw
    if computer == you:
        print('\tIt is a draw!\n')
   
    else:
       # 1(Snake) Possibilities
        if computer == 1 and you == -1:
            print('\tYou Lose!\n')
   
        elif computer == 1 and you == 0:
            print('\tYou Win!\n')
            score[0] += 1
   
       # -1(Water) Possibilities
        elif computer == -1 and you == 1:
            print('\tYou Win!\n')
            score[0] += 1
   
        elif computer == -1 and you == 0:
            print('\tYou Lose!\n')
   
       # 0(Gun) Possibilities
        elif computer == 0 and you == 1:
            print('\tYou Lose!\n')
   
        elif computer == 0 and you == -1:
            print('\tYou Win!\n')
            score[0] += 1
           
       # Nothing Works then
        else:
            print('\tSomething went wrong!\n')
            
    return score 
    
def_score = [0]
score = str(game(def_score))

# Saving & Checking Highest Score
file = 'High_score.txt'
    
if os.path.exists(file):
    with open(file, 'r+') as f:
        hi_score = f.read().replace(' ','')
        
    if hi_score < score: # Updating High Score
        f.write(f'\n{score}\n')
else:
    with open(file, 'w') as f:
        f.write(f'\n{score}\n')

print(f'Your Score: {score}\n')    
