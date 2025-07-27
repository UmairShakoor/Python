
class Employee:
    language = 'CSS' # Class attribute

Umair = Employee() # Object
print(Umair.language)

Employee.language = 'JS' # Changing Class Attribute
print(Umair.language)

Umair.language = 'Python' # instance  attribue takes preference over class attributes

print(Umair.language)
