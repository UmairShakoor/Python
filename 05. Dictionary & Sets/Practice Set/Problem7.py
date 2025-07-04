# if names of 2 friends are same what will happen in problem6 ?

print('\nEnter favourite Programming languages of your friends...\n')

dict = {}

Z_lang = input('Fav lang of Zohaib: ')
K_lang = input('Fav lang of Zohaib: ')
A_lang = input('Fav lang of Ahsan: ')
M_lang = input('Fav lang of Muaz: ')

dict.update({'Zohaib':Z_lang, 'Zohaib': K_lang, 'Ahsan': A_lang, 'Muaz': M_lang})

print(f'\nResult\n\t{dict}\n')


# Answer: In Case of Similiar Keys, The latest update will be counted
