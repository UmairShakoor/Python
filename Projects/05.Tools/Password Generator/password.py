# This program creates a very strong password using `string` and `secrets` modules

import string # Contains strings like alphabets, digits & special chars
import secrets # Gives repeated random numbers (secure)
import random # Give random numbers (not secure)

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

    print('\n\tStrong Password Generator')

    # Input Validation
    while True: # Infinite Loop till we break it
         password_len = input('\nEnter Password Length (min 6): ')

         if not password_len.isdigit(): # If password_len not just contain integers
              print('Invalid Password length, Try Again')
              continue # Go back and restart the loop

         password_len = int(password_len)

         if password_len < 6: # If password_len is smaller than 6
              print('Password length must be at least 6')
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

    print(f'\nYour Password: {password}\n')


