# This Program suggests professional Email Addresses for user

nameInput = input('\nWhat\'s your name: ')
nameLower = nameInput.lower() # Converts the name into lowerCase to handle names written in UpperCase or Capitalized
name = nameLower.replace(' ','') # To remove whiteSpaces from Name

print('\nTop Choices:') # Most Best EmailAdresses

print(f'{name}@{name}.com') # TopEmail
print(f'{name}@gmail.com') # TopGmail
print(f'{name}@proton.me') #TopProton

print('\nBest Alternatives:') # If above not available

print(f'{name}.pro@yourCompany.com') # BestEmail
print(f'{name}.pro@gmail.com') # BestGmail
print(f'{name}.pro@proton.me') # BestTop

print('\n\tNote: Must Avoid using numbers (1,2,3) in your Email Id because it looks UnProfessional.\n')

