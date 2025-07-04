print('\nContact Saver') # Project Name

print('\nCreating Record..') # Process Info

person1 = input('\nName of Person: ').capitalize() # Stores capitalized name of person1
phone_person1 = input(f'Phone Number of {person1}: ') # Phone Number for person1

person2 = input('\nName of Person: ').capitalize()
phone_person2 = input(f'Phone Number of {person2}: ')

person3 = input('\nName of Person: ').capitalize()
phone_person3 = input(f'Phone Number of {person3}: ')

person4 = input('\nName of Person: ').capitalize()
phone_person4 = input(f'Phone Number of {person4}: ')

contacts = {
    person1: phone_person1,
    person2: phone_person2,
    person3: phone_person3,
    person4: phone_person4
}

print('\nCongrats!, Contact Record Created successfuly') # Process Completed

remove_person =  input('\nPerson you wanted to remove: ').capitalize() # Person to remove, capitalized to avoid case-sensitive error

if remove_person in contacts: # Checks if remove_person present in contact list
    contacts.pop(remove_person) # remove the remove_person
    print(f'\n{remove_person} removed from contact list\n')

else: # If not found
    print(f'\n{remove_person} not found in contact list\n')
