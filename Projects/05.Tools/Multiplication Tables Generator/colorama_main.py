import os
from colorama import init, Fore, Style

init(autoreset=True)

def integer_input(input_str):
    while True:
        number = input(Fore.YELLOW + input_str).replace(' ', '')
                        
        if not(number.isdigit()) or number < '0':
            print(Fore.RED + 'Invalid Number')
            continue
                
        number = int(number)
        if number == 0 or number == 1:
            print(Fore.RED + 'Multiplication Tables must starts from 2')
            continue

        if number > 100:
            print(Fore.RED + 'Must be less than or equal to 100')
            continue
        break
        
    return number

def save_table(folder, number, output, table):
    file = f'{folder}/Table of {number}.txt'

    with open(file, 'w') as f:
        for output in table:
            f.write(output)
        f.write('\n')

print(Fore.CYAN + '\n\tMultiplication Tables Generator')

table = []

folder = 'Tables'

if not(os.path.exists(f'{folder}')):
    os.mkdir(f'{folder}')
    
while True:
    multi_boolean = input(Fore.YELLOW + '\nWant to create tables in bulk at once? : ').replace(' ', '').lower()

    if multi_boolean in ['y', 'yes']:
        start_number = integer_input('\nStart Tables from (min 2): ')
        while True:
            end_number = integer_input('End Tables at (max 100): ')

            if end_number <= start_number:
                print(Fore.RED + f'Invalid Input, {end_number} is not greater than {start_number}\n')
                continue
            break
            
        end = integer_input(f'\nTill what end you wanna print each table? (max 100): ')

        print(Fore.GREEN + '\n\tTables are being Generated...')
        for n in range(start_number, end_number+1):
            number = n
            for z in range(1, end+1):
                output = (f'\n{number} X {z} = {number*z}\n')
                table.append(output)

                table = table[-end:]
                save_table(folder, number, output, table)
                
        print(Fore.GREEN + f'\nYour Generated Tables are stored inside {folder} folder\n')
                        
    else:
        number = integer_input('\nWanna table of: ')
        end = integer_input(f'Till what end you wanna print table of {number}? (max 100): ') + 1
        
        for i in range(1, end):
            output = (f'\n{number} X {i} = {number*i}\n')
            table.append(output)

        save_table(folder, number, output, table)
        print(Fore.GREEN + f'\nYour Generated Table is stored inside {folder} folder\n')
        
    break
