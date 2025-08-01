from typing import Dict
import json
import os
from keyStop import msg
from colorama import Fore, Style, init

init(autoreset=True)

def n() -> int:
    while True:
        n: str = input(Fore.CYAN + '\nHow many Tasks you want to add? : ').replace(' ','')

        if n.isdigit():
            return int(n)
        else:
            print(Fore.RED + 'Invalid Number')
            continue

def s(purpose) -> str:
    while True:
        s: str = input(Fore.YELLOW + purpose).strip()

        try:
            int(s)
            print(Fore.RED + 'Invalid Input')
            continue
        except:
            return s

def options() -> None:
    o: Dict[str, str] = {
        'v': 'iew all Tasks',       
        'm': 'ark a Task Done',       
        'd': 'elete a Task',
        's': 'ave all Tasks',
        'e': 'xit'
    }
    
    print(Fore.MAGENTA + '\nWhat would you like to do?')
    print('')

    for command, detail in o.items():
        print(Fore.GREEN + f'[{command}]' + Fore.WHITE + f'{detail}')

def view():
    if not tasks:
        print(Fore.RED + "\nNo tasks found.")
        return

    print(Fore.BLUE + '\nYour Tasks:\n' + '-'*30)
    for title, detail in tasks.items():
        print(Fore.CYAN + f'\n{title}:\n\t' + Fore.WHITE + f'{detail}')        

def task_present(p: str) -> str:
    while True:
        d = input(Fore.YELLOW + f'\nTitle of Task to {p}: ').strip().title()
        if d in tasks:
            return d
        else:
            print(Fore.RED + f'✗ {d} not found. Try again.')

def delete():
    task_title = task_present('delete')
    tasks.pop(task_title)
    print(Fore.GREEN + f"[−] Task '{task_title}' deleted successfully!")

def save():
    file = 'tasks.json'
    with open(file, 'w') as f:
        json.dump(tasks, f, indent=4, sort_keys=True)

    print(Fore.GREEN + f"[✓] Tasks saved to '{file}' successfully!")

def strike_through(text: str) -> str:
    return ''.join(char + '\u0336' for char in text)

def mark():
    m = task_present('mark as Done')
    m_detail = tasks.get(m)
    tasks.pop(m)

    new_title = strike_through(m)
    new_detail = strike_through(m_detail)
    tasks.update({new_title: new_detail})

    print(Fore.GREEN + f'\n[✓] Task ({m}) marked as Done!\n')

def give_options():
    options()
    c = input(Fore.YELLOW + '\nYour Choice: ').strip().lower()

    match c:
        case 's':
            save()
        case 'v':
            view()
        case 'd':
            delete()
        case 'e':
            print(Fore.CYAN + '\nGoodbye! See you soon.\n')
            exit()
        case 'm':
            mark()
        case _:
            print(Fore.LIGHTBLACK_EX + '\nMore features coming soon...')

# Start Execution

tasks: Dict[str, str] = {}

if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    print(Fore.GREEN + '\n[+] Existing tasks loaded from file.\n')
else:
    print(Fore.YELLOW + '\n[-] No previous tasks found.\n')

create_tasks: int = n()

for i in range(1, create_tasks + 1):
    print(Fore.CYAN + f'\n--- Task {i} ---')
    title: str = s('\nTitle: ').title()
    detail: str = s('Detail: ').capitalize()
    tasks.update({title: detail})

print(Fore.GREEN + '\n[+] Your Tasks have been Created.')

# Initial Option
give_options()

# Repeat Options
while True:
    more = input(Fore.YELLOW + '\nDo more? (y/n): ').strip().lower()
    if more in ['y', 'yes']:
        give_options()
    else:
        print(Fore.CYAN + '\nGoodbye! See you soon.\n')
        exit()
