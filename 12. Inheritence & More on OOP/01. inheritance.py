class Employee: # Base Class
    company = 'Microsoft'
    def show(self):
        print(f'The name of Employee is {self.name}')

# class Programmer:
#     def show(self):
#         print(f'The name is {self.name} and salary is {self.salary}')
# 
#     def showLang(self):
#         print(f'Language is: {self.language}')

class Programmer(Employee): # Inherited Class
    company = 'Google'
    def showLang(self):
        print(f'Language is: {self.language}')
        
a = Employee()
b = Programmer()

print(a.company, b.company)
