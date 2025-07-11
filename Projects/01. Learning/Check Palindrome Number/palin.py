# This program checks if a number is palindrome (same forwards and backwards)

number = input('\nNumber: ')
number_reversed = number[::-1] # Reverse all characters of string

if number == number_reversed:
     print(f'{number} is a Palindrome')

else:
     print(f'{number} is not a Palindrome')
