
class Employee:
    language = 'Python' # Class attribute
    salary = 1200000

    def getInfo(self):
        print(f'Language: {self.language}\nSalary: {self.salary}')

    @staticmethod # It says we are just using function without any object/class attribute (This can be called without any argument)
    def greet():
        print('Good Morning')
    
harry = Employee() # Object
harry.language = 'JS' # instance  attribue

harry.getInfo() # it means Employee.getInfo(harry)
harry.greet()
