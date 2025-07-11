'''
a = 5
b = 40
c = 8

average = ( a + b + c ) / 3
print(average)

a = 50
b = 4
c = 88

average = ( a + b + c ) / 3

print(average) '''

# Functions are used to name a piece of logic

# Function Defination
def avg(): # Defines a function
    a = int(input('Number1: '))
    b = int(input('Number2: '))
    c = int(input('Number3: '))

    average = (a+b+c) / 3
    print('Average:', average)

# Function Call
avg() # Tells to run avg() funtion
avg()
avg()
avg()

# Function Types
# 1. Built-in-functions (Already present in Python)
# 2. User-defined-functions (Defined by the user)
