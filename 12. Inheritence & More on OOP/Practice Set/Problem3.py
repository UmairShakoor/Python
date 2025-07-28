#  Create a class 'Employee' and add salary and increment properties to it

class Employee:
    salary = 10238
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return int(self.salary + self.salary*(self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = int((salary/self.salary) - (1 * 100))
        
e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2340
print('Increment =', e.salaryAfterIncrement)
