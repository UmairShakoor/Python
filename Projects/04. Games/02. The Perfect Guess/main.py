from random import randint

def _input():
    while True:
        a = input('\nGuess the number: ').strip()

        if a.isdigit():
            break

        else:
            print('Invalid Input')
            continue

    return int(a)
    
n = randint(1, 100)

a = -1 # Just to start the loop
guesses = 1

print('\n\tThe Perfect Guess')
while (a != n):
    a = _input()

    if (a > n):
        print('Lower Number Please.')
        guesses += 1
        
    elif (a < n):
        print('Higher Number Please.')
        guesses += 1
    
print(f'\nCongrats!, You have guessed the number in {guesses} attempts\n')

