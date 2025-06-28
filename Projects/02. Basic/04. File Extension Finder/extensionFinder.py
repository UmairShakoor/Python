# This Program tells you the extension of file.extension that user has given

file = input('\nEnter fileName with Extension (e.g, file.txt): ')

separatorIndex = file.find('.') # Index of '.' which separates fileName & fileExtension
extensionIndex = separatorIndex + 1 # Index of fileExtension

extension = file[extensionIndex:] # Gives fileExtension by slicing from extensionIndex to end (Total Length)

if '.' in file: # Prints fileExtension if separator '.' found in file
    print(f'Extension: {extension}\n')

else: # Prints Message if separator '.' not found in file
    print('Extension not Found\n')


