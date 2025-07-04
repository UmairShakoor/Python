# Sum a list of 4 numbers

print('\nEnter 4 Numbers to find Sum..')

n1 = int(input('\nFirst Number: '))
n2 = int(input('Second Number: '))
n3 = int(input('Third Number: '))
n4 = int(input('Fourth Number: '))

numbers = [n1, n2, n3, n4]

total  = sum(numbers) # sum() is a function to sum all numbers of a list

print(f'\nSum: {total}\n')
