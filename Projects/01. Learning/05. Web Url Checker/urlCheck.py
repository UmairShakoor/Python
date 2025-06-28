# This program checks if user gives valid or invalid Web URL

url = input("\nEnter Complete Web URL: ")

if (url.startswith('https://') or url.startswith('http://')): # Checks if URL startsWith https:// or http://
   print('Valid URL\n')

else: # Checks if URL not startsWith https:// or http://
   print('Invalid URL\n')
