class Employee:
    def __init__(self):
        print('Constructer of Employee')
    a = 1

class Programmer(Employee):
    def __init__(self):
        print('Constructer of Programmer')
    b = 2

class Manager(Programmer):
    def __init__(self):
            super().__init__() # Runs Constructer of Parent also
            print('Constructer of Manager')
    c = 3
     
# o1 = Employee()
# o2 = Programmer()
o3 = Manager()
