# Create a class (2-D vector) and use it to create another class representing a 3-D vector

class D2:
    def __init__(self):
        self.i = 'i'
        self.j = 'j'

class D3(D2):
    def __init__(self):
        super().__init__()
        self.k = 'k'
        
v = D3()
print(v.i, v.j, v.k)
