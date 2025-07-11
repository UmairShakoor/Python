# This program first stores a password from user and keep asking again till the user enter the correct password but exhausts after 3 attempts

print('\n\tPassword Authenticator')

saved_password = input('\nSave Password: ')
re_enter_password = input('Re-enter your Password: ')

while ( saved_password != re_enter_password ) :
    print('\nPassword not saved. Save password again!!..')
    saved_password = input('\nSave Password: ')
    re_enter_password = input('Re-enter your Password: ')

print('\nPassword Saved, Successfuly! and ready for Password Authentication...')

password = input('\nEnter your Password: ')

for i in range(1, 4):
    if (password == saved_password):
        print('\nPassword Authentication Successful!. Congrats...\n')
        break

    else:
        if i == 3:
             print('\nLast attempt remaining! Be careful...')
        else:
             print(f'\nPassword Incorrect!. {i} Attempt(s) gone, Try Again...')

        password = input('\nEnter your Password: ')

else:
    print('\nYou are out of Attempts. Please, Try Again later...\n')

