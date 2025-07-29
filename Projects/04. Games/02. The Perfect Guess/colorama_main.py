from colorama import Style,init,Fore
init(autoreset=True)

from random import randint

def _input():
    while True:
        a = input(Fore.CYAN + Style.BRIGHT + '\nGuess the number: ').strip()

        if a.isdigit():
            break

        else:
            print(Fore.RED + 'Invalid Input')
            continue

    return int(a)
    
n = randint(1, 100)

a = -1 # Just to start the loop
guesses = 1

print(Fore.CYAN + '\n\tThe Perfect Guess')

while (a != n):
    a = _input()

    if (a > n):
        print(Fore.YELLOW + 'Lower Number Please.')
        guesses += 1
        
    elif (a < n):
        print(Fore.YELLOW + 'Higher Number Please.')
        guesses += 1
    
print(Fore.GREEN + Style.BRIGHT + f'\nCongrats!, You have guessed the number in {guesses} attempts\n')
