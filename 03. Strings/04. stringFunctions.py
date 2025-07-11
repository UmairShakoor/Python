name = "umair"
print(len(name)) # len() gives the length of a string

print(name.endswith('ir')) # .endswith() tells either the shortString is at the end of a string
print(name.startswith('U')) # .startswith() tells either the shortString is at the start of a string

print(name.capitalize()) # return capitalized (First character capital) string

string = "HEllO"
print(string.lower()) # returns lowered (All characters of first word in lowerCase) string
print(string.upper()) # returns uppered (All characters of first word in upperCase) string

makeTitle = "this can be the title"
print(makeTitle.title()) # returns titled (All first characters of all words in upperCase) string

index = makeTitle.find('the') # .find() gives the index of first character of shortString in a string for the first time
print("index of the is:", index)

countE = makeTitle.count('e') # .count() counts the total number of occurance of a substring
print(countE)

a = "Umair is a good boy"
print(a.replace('good', 'bad')) # .replace() replaces a shortString with a given shortString

# .replace(' ','') removes all white spaces from starting , ending & inside the string
# .strip() removes all white spaces from starting & ending of string
