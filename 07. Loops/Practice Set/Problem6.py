# Write a program to calculate the factorial of a given number using for loop.

n = int(input('\nNumber: '))

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print(f'\nFactorial of {n} is: {factorial}')

