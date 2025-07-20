'''
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder
'''

import os

if os.path.exists('Tables'): # If 'Tables' exists)
    os.system('rm -r Tables') # Remove folder 'Tables'

os.mkdir('Tables') # Create folder 'Tables'

print('\n\tGenerating Multiplication Tables of 2 - 20...') # Process Info

def generate_tables(n):
    with open(f'Tables/Table of {n}.txt', 'w') as f:
        for i in range(1, 11):
            f.write('\n')
            f.write(f'{n} X {i} = {n*i}')
        f.write('\n\n')

print('\nTables Generated Successfully!\n') # Process Completed
    
for i in range(2, 21):
    generate_tables(i)
