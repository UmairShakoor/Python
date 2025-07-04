'''  Write a program to find whether a given username contains less than 10
characters or not '''

username = input('\nUsername: ')
char_username = len(username)

if char_username < 10:
    print('\nLess than 10 characters\n')

else:
    print('\nMore than 10 characters\n')

