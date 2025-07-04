# Write a Program that takes 8 numbers from user and display them , unique (No repitition)

print('\nGive 8 numbers to display them uniquely..\n')

n1 = input('First no: ')
n2 = input('Second no: ')
n3 = input('Third no: ')
n4 = input('Fourth no: ')
n5 = input('Fifth no: ')
n6 = input('Sixth no: ')
n7 = input('Seventh no: ')
n8 = input('Eighth no: ')

numbers = set() # Empty Set of numbers
numbers.update(n1, n2, n3, n4, n5, n6, n7, n8)

print(f'\nYour Unique Numbers:\n\t{numbers}\n')

