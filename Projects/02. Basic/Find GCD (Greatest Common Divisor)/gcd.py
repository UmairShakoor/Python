# This program gives the GCD (Greatest Common Divisor) of 2 numbers

print('\nGCD Calculator') # Project Name

number1 = int(input('\nFirst Number: '))
number2 = int(input('Second Number: '))

factors1 = []
factors2 = []

for i in range(1, (number1 // 2) + 1):
     if (number1 % i == 0):
           factors1.append(i)

for i in range(1, (number2 // 2) + 1):
      if (number2 % i == 0):
           factors2.append(i)

common_factors = []

for i in factors1:
      if i in factors2:
            common_factors.append(i)

gcd = max(common_factors)

print(f'\nGCD of {number1} and {number2} is: {gcd}\n')
