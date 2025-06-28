# This Program Hides a Password from user

password = input('\nEnter a password to Hide: ')

passLen = len(password)
keys = ("*")*passLen

hiddenPass = password.replace(password,keys)
print(f'Your Hidden Password is: {hiddenPass}\n')
