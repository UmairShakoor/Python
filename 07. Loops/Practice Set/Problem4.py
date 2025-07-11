# Write a program to find whether a given number is prime or not

number = int(input('\nNumber: '))

if number <= 0:
    print(f'\n{number} is NOT a Prime Number')

else:
    is_prime = True # Assume it is prime

    for i in range(2, number):
        if number % i == 0:
            is_prime = False # Bcz number has a divisible
            break

    if is_prime:
        print(f'\n{number} is a Prime Number\n')
    else:
        print(f'\n{number} is NOT a Prime Number\n')
