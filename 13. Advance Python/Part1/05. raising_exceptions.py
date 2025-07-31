a = int(input('Enter a number: '))
b = int(input('Enter second number: '))

if (b == 0):
    raise ZeroDivisionError('Hey, Our program is not meant to divide by 0') # Crash the program and print custom error message

else:
    print(f'a / b = {a/b}')
