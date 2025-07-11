# This Program calculates factorial of a given number using recursions

from colorama import Fore, Style, init # For Colorful & Clean UI in terminal

if __name__ == '__main__':

    # Initialize colorama for Windows compatibility
    init(autoreset=True)

    # Header (Project Name)
    print(Fore.BLUE + Style.BRIGHT + '\n======================================')
    print(Fore.CYAN + Style.BRIGHT + '    Factorial Calculator')
    print(Fore.BLUE +  '======================================')

    # Input Validation
    while True: # Inifinte Loop till we break it
        number = input(Fore.WHITE + '\nEnter Number: ')

        if not number.isdigit(): # If number not just contain digits
                print(Fore.RED + 'Invalid Number, Enter a valid number')
                continue # Go back and restart the loop

        number = int(number) # Convert number(string) to an integer(digit)

        if number < 0: # If number is less than 0 (negative)
                print(Fore.RED + 'Invalid Number, Enter number greater than or equal to 0')
                continue

        break # If everything is Ok

    # Input Validation Completed and start to calculate factorial
    def factorial(number): # Defining factorial() function

        if (number == 1) or (number == 0): # If number is 0 or 1
                return 1 # Bcz factorial of 0 or 1 is '1' (Maths Rule)

        return number * factorial(number - 1) # Recursion using Mathematical Formula

    factorial = factorial(number)
    print(Fore.YELLOW + Style.BRIGHT + '\nFactorial of', Fore.RED + f'{number}', Fore.GREEN + 'is:', Fore.CYAN + Style.BRIGHT + f'{factorial}\n')
