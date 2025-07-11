# if languages of 2 friends are same then what will happen in problem6?

print('\nEnter Favourite Programming languages of your friends...\n')

dict = {}

Z_lang = input('Fav lang of Zohaib: ')
A_lang = input('Fav lang of Ahsan: ')
M_lang = input('Fav lang of Muaz: ')

dict.update({'Zohaib': Z_lang, 'Kamran': Z_lang, 'Ahsan': A_lang, 'Muaz': M_lang})

print(f'\nResult\n\t{dict}\n')

# Answer: In Case of Similiar Values of different keys , Both exist with their similiar value
