# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the 'ZeroDivisionError'

try:
    a = int(input('\nNumber1: '))
    b = int(input('Number2: '))

except Exception as e:
    print('Invalid Input')
    exit()

try:
    c = int(a / b)
    print(f'{a} / {b} = {a/b}')

except ZeroDivisionError:
    print(f'{a} / {b} = infinite (Undefined)')
