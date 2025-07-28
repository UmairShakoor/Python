def valid_number(no):
    while True:
        print('')
        n = input(f'Number{no}: ')

        if n.isdigit():
            break
            
        else:
            print('Invalid Number')
            continue
    return n

n1 = valid_number(1)

cal_method = ['+', '-', '*', '/', '%', '//', '**']

while True:
    method = input('\nMethod: ').replace(' ','')

    if not(method in cal_method):
        print('Method not defined')
        continue
    break
    
n2 = valid_number(2)

result = eval(f'{n1} {method} {n2}') # eval() is used to perform calculation on strings

print(f'\n{n1} {method} {n2} = {int(result)}\n')
