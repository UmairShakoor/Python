# Recursion: A function that continue to calling itself till the condition/formula compeletes

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * 1
factorial(3) = 3 * 2 * 1
factorial(4) = 4 * 3 * 2 * 1
factorial(5) = 5 * 4 * 3 * 2 * 1

factorial(n) = n * n-1 * n-2 ... * 3 * 2 * 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if (n==1 or n==0): # Base condition to stop/end recursion
        return 1
    return n * factorial(n-1) # Recursion

n = int(input('Enter a Number: '))
print(f'Factorial of {n} is: {factorial(n)}')

