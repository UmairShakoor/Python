# Write a program using functions to find greatest of three numbers

def max_number(a, b, c):
    if a>b and a>c: # If a is greatest
        return a

    elif b>a and b>c: # If b is greatest
        return b

    elif c>a and c>b: # If c is greatest
        return c

a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))

print(f'\nGreatest Number is: {max_number(a, b, c)}\n')
