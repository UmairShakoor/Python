''' Write a program to print the following star pattern.
  *
 ***
***** for n = 3 '''

n = int(input('\nNumber: '))

for i in range(1, n+1):
    print(' ' * (n - i), end="") # print() starts from new line by default , end="" forces print to start in the same line
    print('*' * (2*i - 1), end="")
    print('') # Adds new line
