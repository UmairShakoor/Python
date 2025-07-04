# Lists can store any type of data inside sqaure brackets []

list = ['Apple', 'Orange', 5, 35.06, 'False', None] # <class 'list'>

print(f'{list} is {type(list)}') # Fancy Strings allows to add variables in strings enclosed inside {}

print(list[0]) # Lists can be indexed just like Strings

list[0] = 'Grapes' # Lists are Mutable (we can update them using assignement operators) but strings are imutable and all functions of strings directly updates the list but string functions just return a new string not update the existing string
print(list[0]) # Updated list[0] = 'Grapes'

print(list[1:4])
