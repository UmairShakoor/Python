# This program list all the factors of a number

print('\n\tFactor Counter') # Project Name

number = int(input('\nNumber: '))

for i in range(1,( number // 2) + 1): # No number bigger than half of a number can be its factor . So, I used `number // 2` to speed up the program
     if ( number % i == 0) :
         print(i)
print(number)
