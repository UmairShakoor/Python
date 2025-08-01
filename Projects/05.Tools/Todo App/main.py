from typing import Dict
import json
import os
from keyStop import msg

def n() -> int:
    while True:
        n: str = input('\nHow many Tasks you want to add? : ').replace(' ','')

        if n.isdigit():
            return int(n)
            
        else:
            print('Invalid Number')
            continue

def s(purpose) -> str:
    while True:
        s: str = input(purpose).strip()

        try:
            int(s)
            print('Invalid Input')
            continue

        except:
            return s

def options() -> str: # Print all options
    o: Dict[str, str] = {
        'v': 'iew all Tasks',       
        'm': 'ark a task Done?',       
        'd': 'elete a Task',
        's': 'ave all Tasks?',
        'e': 'exit'
    }
    
    print('\nWhat you would like to do? : ')
    print('')
    
    for command, detail in o.items():
         print(f'[{command}]{detail}')

def view(): # Print all tasks
    for title, detail in tasks.items():
        print(f'\n{title}:\n\t{detail}')        

def task_present(p: str) -> str: # Check if a task is present
    while True:
        d = (input(f'\nTitle of Task you want to {p}: ').strip()).title()
        try:
            tasks[d]
            return d
        except:
            print(f'{d} don\'t match any Task')
            continue
            
def delete(): # Deletes a task
    task_title = task_present('delete')
    tasks.pop(task_title)
    print(f"Task '{task_title}' has been deleted successfuly!")

# Save Command
def save():
    file = 'tasks.json'
    with open(file, 'w') as f: # Writing tasks into file
            json.dump(tasks, f, indent=4, sort_keys=True) # Write tasks in json format with indent space 4 and also sort alphabatically

    print(f"Your tasks have been saved into '{file}' Successfully!")
    
# Task Completed
def strike_through(text: str) -> str: # Strike Through a string
    return ''.join(char + '\u0336' for char in text)
    
def mark():
    m = task_present('mark as Done')
    m_detail = tasks.get(m)
    tasks.pop(m) # Delete old task

    new_title = strike_through(m)
    new_detail = strike_through(m_detail)
    tasks.update({new_title: new_detail}) # Add marked (strike through) task

    print(f'\nCongrats on Completing Task ({m}). Now, it has marked Done!\n')

def give_options():
    options() # Print all options
    
    c = (input('\nYour Choice: ').strip()).lower()    
    
    match(c):
        case 's':
            save()
        case 'v':
            view()
        case 'd':
            delete()
        case 'e':
            print('\nGoodBye!, See you soon.\n')
            exit()
        case 'm':
            mark()
        case _:
            print('\nMore Features are Coming Soon...')
                
# Exection Starts from here

tasks: Dict[str, str] = {}

if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    print('\nExisting tasks loaded from file.\n')
else:
    print('\nNo previous tasks found.\n')
   
create_tasks: int = n()

for i in range(1, create_tasks+1):
    print(f'\n--- Task {i} ---')
    
    title: str = s(f'\nTitle: ').title()
    detail: str = s(f'Detail: ').capitalize()    

    tasks.update({title: detail})
    
print('\nYour Tasks have been Created')

# Execution of Options
give_options()

# Perform Something more
while True:
    more = (input('\nWanna perform something more? (y|n): ').strip()).lower()

    if more in ['y', 'yes']:
        give_options()

    else:
        print('\nGoodBye, See you soon.\n')
        exit()
