# Create an empty dict. Allow 4 friends to enter their favourite language as value and their names as keys. Assume that names are unique

print('\nEnter Favourite Programming languages of your friends..')

dict = {}

Z_lang = input('\nFavourite language of Zohaib: ')
K_lang = input('Favourite language of Kamran: ')
A_lang = input('Favourite language of Ahsan: ')
M_lang = input('Favourite language of Muaz: ')

dict.update({'Zohaib': Z_lang, 'Kamram': K_lang, 'Ahsan': A_lang, 'Muaz': M_lang})

print(f'\nResult:\n\t{dict}\n')
