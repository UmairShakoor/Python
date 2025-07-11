print('\nAccount Info Display') # Project Name

print('\n\tStoring your Account Info......') # Process info

username_input = input('\nYour Username: ').lower() # Store username in lowercase
username = username_input.replace(' ','') # Removes white spaces

email_input = input('Your Email: ').lower()
email = email_input.replace(' ','')

password = input('Your Password: ')

info = {
    'UserName': username,
    'Email': email,
    'Password': password
}

print(f'\nYour Account info is: \n\t {info}\n') # Final Result (Display Account Info)
