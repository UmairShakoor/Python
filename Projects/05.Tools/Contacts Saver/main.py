# First, install `pip install phonenumbers` module to run this program

import phonenumbers # phoneNumbers module used to validate phoneNumber
import sys # Built-in Module to perform system-specific actions 

# Functions

def contacts_len(purpose): # Contacts_len Function
    while True:
        length = input(f'\nHow many Contacts you want to {purpose}? (Max 10): ').replace(' ','')
    
        if not(length.isdigit()) or length <= '0': # If contacts_len is not a digit or less than/equal to 0
            print('Invalid Number')
            continue
    
        length = int(length)
        
        if length > 10: # If exceeds limit
            print(f'Can {purpose} maximum 10 contacts at a time!')
            continue
        
        break
    return length

def contact_input(): # Contact Input Function

    while True: # Contact Name input
        contact_name = (input('\nContact Name: ').strip()).title()
    
        if contact_name.isdigit() or contact_name < '0': # If contact is a number
            print('Invaid Contact Name')
            continue
                
        break
    
    while True: # Phone Number Input
        phone_number = input(f"{contact_name}'s Phone Number with Country Code (e.g, +923001234567): ").replace(' ','')

        if phone_number.startswith('+') and phonenumbers.is_possible_number_string(phone_number, None): # if phone_number startswith + and is a valid phoneNumber according to country code
            parsed = phonenumbers.parse(phone_number, None) # Break it to something like PhoneNumber(countryCode=92, NationalNumber=3001234567)
            phone_number = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL) # Formats parsed phoneNumber (+92 3001234567)

            if not(phonenumbers.is_valid_number(parsed)):# Not(Is this phone_number could exit in the given country code and recognized pattern + registered?)
                print('Invalid Phone Number')
                continue
            
        else:
            print('Invalid Phone Number, Must start with + and be a real phone number')
            continue
            
        break
    return contact_name, phone_number
    
def create_contacts(purpose, contacts_len): # Create Contacts Function
    for contact in range(1, contacts_len+1):# Loop to create contacts_len contacts
        print(f'\n\t... Contact {contact} ...')

        contact_name, phone_number = contact_input()                          
                                      
        # Saving Contacts
        contacts.update({
            contact_name: phone_number
        })
               
    print(f'\nCongrats!, Contacts {purpose}ed successfuly') # Process Completed

def options():
    options_dict = {
        'v': 'iew Contacts',
        'a': 'dd Contacts',
        'f': 'ind Contact',
        'r': 'emove Contact',
        's': 'ave Contacts',
        'q': 'uit'
    }
    for command, option in options_dict.items():
        print(f'[{command}]{option}')

def find_contact(): # find/search contact function
    find_contact = (input('\nContact Name you wanna Search: ').strip()).title()

    if find_contact in contacts:
        print(f"\n'{find_contact}': {contacts[find_contact]}")

    else:
        print(f"\n'{find_contact}' not found!")
        
def view_contacts(): # View all contacts function
    print('') # Adds New line
    
    for name, contact in contacts.items():
        print(f'{name}: {contact}')
        
def remove_contact():
    remove_contact = (input('\nContact Name you wanna remove: ').strip()).title()

    if remove_contact in contacts:
        contacts.pop(remove_contact) # Remove Contact
        print(f"\n'{remove_contact}' removed successfully!")
        print(f'\nRemaining Contacts: ')
        view_contacts() # View Remaining Contacts

    else:
        print(f"\n'{remove_contact}' not found!")

def save_contacts():
    file_name = input('\nEnter file Name you want to save with (e.g, contacts.txt): ').strip()
        
    with open(file_name, 'w') as file: # Creates Contacts.txt in current folder
        file.write('\nContacts List...\n') # Heading of File
        for name, contact in contacts.items():
            file.write(f'{name}: {contact}\n') # Write Name and Contact one by one
        file.write('\n') # Adds New line at the end
            
    print(f"Your Contacts have been saved to '{file_name}'\n")

def add_contacts(purpose): # Add contacts Function
    contacts_length = contacts_len(purpose)
    create_contacts(purpose, contacts_length)

def quit(): # Exit/quit program Function
    # If contacts are edited but not saved
    if created_contacts_len < len(contacts):
        edited_save = (input('\nYou have unsaved changes. Do you want to save them? (y|n): ').replace(' ','')).lower()
    
        if edited_save in ['y', 'yes']:
            save_contacts()
            print('')
            
        else:
            print('\nGoodbye!\n')
            sys.exit(0)
            
    else:
        print('\nGoodbye!\n')
        sys.exit(0) # Quit Program with status code 0 (Success)

# Input/Output Starts ...
print('\n******************************')
print('\tContacts Saver') # Project Name
print('******************************')

print('\nCreating Contacts ...') # Process Info

contacts = {} # Dict to contain contacts

contacts_length = contacts_len('create') # Input for contacts_len
create_contacts('creat', contacts_length) # Creating Contacts

created_contacts_len = len(contacts)

# Features/Options
print('\nWhat would you like to do?\n')
options() # Calling Options Function
print('')

# Option Input
while True:
    option = (input('\nEnter you choice: ').replace(' ','')).lower()

    if option == 'v':
        view_contacts()
        print('')

    elif option == 'a':
        add_contacts('add')
        print('')

    elif option == 's':
        save_contacts()
        print('')

    elif option == 'r':
        remove_contact()

    elif option == 'f':
        find_contact()
        print('')

    elif option == 'q':
        quit()

    else:
        print('\nInvalid Input')
        continue

    break
