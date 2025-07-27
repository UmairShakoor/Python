# Classes are like blank forms to fill details (data) . A single class can be used to create multiple object (like forms with data filled in it) like the copies of a blank form

class Employee:
    language = 'Python' # Class attribute
    salary = 1200000

Umair = Employee() # Object
Umair.name = 'Umair' # instance  attribue
print(Umair.name, Umair.language, Umair.salary)

Harry = Employee()
Harry.name = 'Harry'
print(Harry.name, Harry.language, Harry.salary)


# Here name is the instance attribute and language + salary are class attributes as they directly belongs to the class

