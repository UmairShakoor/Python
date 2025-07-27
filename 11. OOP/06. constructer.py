
class Employee:
    language = 'JS' # Class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method that automatically calls itself
        self.name = name # Setting instace attributes
        self.salary = salary
        self.language = language
        print('I am a dunder method')
    
Umair = Employee('Umair', 'Unlimited', 'Python') # Object
print(Umair.name, Umair.language, Umair.salary)

# rohan = Employee()
