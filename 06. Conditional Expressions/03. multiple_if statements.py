age = int(input('Enter your age: '))

# if statement 1

if (age%2 == 0):
    print('age is even')

# End of if statement 1

# if statement 2

if (age >= 18): # If age greater than or equals to 18
    print('You are above the age of consent')
    print('Good for your')

elif (age < 0): # if age is smaller than 0
    print('Age can\'t be negative')

elif (age == 0): # if age is equal to 0
    print('Are you kidding')

else: # if all false
    print('You are below the age of consent')

# End of if statement 2
