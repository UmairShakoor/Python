''' Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def star_pattern(n):
    if n == 0:
        return # Just don't execute the following lines in function and exit

    print('*' * n)
    star_pattern(n-1) # Recursion


n = int(input('Enter Number: '))
star_pattern(n)
