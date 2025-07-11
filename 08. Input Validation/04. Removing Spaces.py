# Some users input extra or unnecessary spaces that may disturb the program or results in un-accurate data . So, we have to remove that spaces..

# Spaces at the end and start of input

spaced_name = input('Enter your name: ') # Consider input is `  Name  `
print(len(spaced_name)) # Output: 8

exact_name = spaced_name.strip() # .strip() remoevs all spaces from start and end of string
print(len(exact_name)) # Output: 4

# Spaces inside data

input_username = input('Enter your username: ').lower() # Consider input is `  Rohan Das  `
stripped_username = input_username.strip() # .strip() has removed spaces around data
print(stripped_username) # Output: `rohan das`

actual_username = input_username.replace(' ','') # .replace(' ','') will remove all spaces from string either around it (start & end) or inside
print(actual_username) # Output: `rohandas`
