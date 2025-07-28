class Employee: # Base\Parent Class1
    company = 'Microsoft'
    def show(self):
        print(f'The name of Employee is {self.company}')

class Coder: # Parent Class2
    language = 'Python'
    def printLanguages(self):
        print(f'Out of all the languages here is your language: {self.language}')
    
class Programmer(Employee, Coder): # Inherited Class from two Parent Classes
    company = 'Google'
    language = 'JS'
    def showLang(self):
        print(f'Language is: {self.language}')
        
a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLang()
