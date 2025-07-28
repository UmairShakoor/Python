class Employee():
    a = 1

    @classmethod # Now it shows class attributes value not instance value
    def show(self):
        print(f'The class attribute a is {self.a}')

e = Employee()
e.a = 45

e.show()
