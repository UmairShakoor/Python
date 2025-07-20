import os

def integer_input(input_str):
    while True:
        number = input(input_str).replace(' ','')
                        
        if not(number.isdigit) or number < '0':
            print('Invalid Number')
            continue
                
        number = int(number)
        if number == 0 or number == 1: # If number is 0 or 1
            print('Multiplication Tables must starts from 2')
            continue

        if number > 100:
            print('Must be less than or equal to 100')
            continue
        break
        
    return number

def save_table(folder, number, output, table): # Save table in different files
    file = f'{folder}/Table of {number}.txt'

    with open(file, 'w') as f:
        for output in table: # Iterating each output in table
            f.write(output)
        f.write('\n')
        
print('\n\tMultiplication Tables Generator') # Project Name

table = []

# Saving files in folder
folder = 'Tables' # Folder name

if not(os.path.exists(f'{folder}')): # If not(folder already exists)
    os.mkdir(f'{folder}') # Make folder
    
while True:
    multi_boolean = (input('\nWant to create tables in bulk at once? : ').replace(' ','')).lower()

    if multi_boolean in ['y', 'yes']:
        start_number = integer_input('\nStart Tables from (min 2): ')
        while True:
            end_number = integer_input('End Tables at (max 100): ')

            if end_number <= start_number:
                print(f'Invalid Input, {end_number} is not greater than {start_number}\n')
                continue
            break
            
        end = integer_input(f'\nTill what end you wanna print each table? (max 100): ')

        print('\n\tTables are being Generated...')
        for n in range(start_number, end_number+1):
            number = n
            
            for z in range(1, end+1):
                output = (f'\n{number} X {z} = {number*z}\n') # Table
                table.append(output)

                table = table[-end:] # Slices lastest {end} number of  strings
                save_table(folder, number, output, table) # Run Function
                
        print(f'\nYour Generated Tables are stored inside {folder} folder\n')
                        
    else:
        number = integer_input('\nWanna table of: ') # Call the function and stores number
        end = integer_input(f'Till what end you wanna print table of {number}? (max 100): ') + 1
        
        for i in range(1, end):
            output = (f'\n{number} X {i} = {number*i}\n') # Table
            table.append(output)

        save_table(folder, number, output, table) # Run Function
        print(f'\nYour Generated Table is stored inside {folder} folder\n')
        
    break

