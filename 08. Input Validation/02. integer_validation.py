# We can convert string's input to any other dataType , Most common conversion is to integer.

# age = int(input('Enter your age: '))
# Your program will crash if user enters abc..

# To avoid crash we have to verify if the input is integer before converting input() to integer

age = input('Enter you age: ')

# .isdigit() checks if string is made of integers only . It returns False even if string contains a floating point number
# .isdigit() is very strict and returns False even string contains a space.
if age.isdigit():
    age = int(age)
    print(f'Thanks, Age Recorded: {age}')

else:
    print('Invalid Age, Age must be an integer')

# .isalnum() is a function to check either a string just contains of alphabets or numbers
