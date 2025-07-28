# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'

class Animals:
    def __init__(self):
        self.a1 = 'cat'
        self.a2 = 'lion'
        self.a3 = 'sparrow'

class Pets(Animals):
    pass
    
class Dog(Pets):
    def bark(self):
        print(f'{(self.a2).title()} is Barking')

b = Dog()
b.bark()
