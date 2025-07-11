# Write a program to print multiplication table of n using for loops in reversed order

n = int(input('\nNumber: '))

for i in range(1, 11):
    print(n * (11-i))
