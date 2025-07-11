# This program creates a very strong password using `string` and `secrets` modules

import string # Contains strings like alphabets, digits & special chars
import secrets # Gives repeated random numbers (secure)
import random # Give random numbers (not secure)
from colorama import Fore, Style, init # For Colorful & Clean UI in terminal

if __name__ == '__main__':

    lower_alphabets = list(string.ascii_lowercase)
    upper_alphabets = list(string.ascii_uppercase)

    integers = list(string.digits)

    special_chars = list(string.punctuation)

    pass_keys = []
    pass_keys.extend(lower_alphabets) # .extend() adds each element of a list to another list
    pass_keys.extend(upper_alphabets)
    pass_keys.extend(integers)
    pass_keys.extend(special_chars)

    # Initialize colorama for Windows compatibility
    init(autoreset=True)

    # Header (Project Name)
    print(Fore.BLUE + Style.BRIGHT + '\n======================================')
    print(Fore.CYAN + Style.BRIGHT + '       Strong Password Generator')
    print(Fore.BLUE +  '======================================')

    # Input Validation
    while True: # Infinite Loop till we break it
         password_len = input(Fore.GREEN + "\nEnter Password Length (min 6): ")

         if not password_len.isdigit(): # If password_len not just contain integers
              print(Fore.RED + 'Invalid input! Please enter a number.')
              continue # Go back and restart the loop

         password_len = int(password_len)

         if password_len < 6: # If password_len is smaller than 6
              print(Fore.RED + 'Password must be at least 6 characters')
              continue

         break # If password_len just contain digits then exit the loop now

    # Input is Valid, Now Password Making start...

    password_list = [ # Must require atleast one of every type
           secrets.choice(lower_alphabets), # One lower case aplhabet
           secrets.choice(upper_alphabets), # One upper case aplhabet
           secrets.choice(integers), # One digit
           secrets.choice(special_chars), # One special char aplhabet
    ]
    remaining_len = password_len - 4
    password_list +=  list(''.join(secrets.choice(pass_keys) for _ in range (remaining_len)))
    random.shuffle(password_list)

    password = ''.join(password_list)

    # Display Output
    print(Fore.GREEN + Style.BRIGHT + '\nYour Password: ' + Fore.CYAN + Style.BRIGHT + f'{password}\n')
