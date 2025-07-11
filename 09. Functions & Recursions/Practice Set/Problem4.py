# Write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if n==0:
        return '0 is not a natural number'
    if n==1:
        return 1
    return n + sum(n-1) # Recursive funtion that repeats itself

n = int(input('Sum of first natural numbers: '))
print(f'Sum is: {sum(n)}')
