# Anything written inside quotes is called as 'String'

a = 'Umair' # Single Quote String
b = "Umair" # Double Quote String
c = '''Umair''' # Triple Single Qoute String
d = """Umair""" # Triple Double Qoute

print(a,b,c,d)

# Strings are Immutable means you can't change them using function instead functions create another string

# Strings Slicing :

# Indexing of String

name = "Umair" # it represented in index(counting) as "01234" . We can also index it in negative integer and it starts from end So : 4 = -1 , 3 = -2 , 2 = -3 , 1 = -4 and 0 = -5
# Remember, reverse counting dosen't starts with 0 !!

character1 = name[0] # Gives character at 0 Index
print(character1)

shortName = name[0:3] # Starts from index 0 to 3 but not including 3 . Syntax ; name[index_start:index_end]
print(shortName)

nameLength = len(name) # it gives length of name which is the number of characters in the string
print(nameLength)
