class Number:
    def __init__(self, n1):
        self.n1 = n1

    def __add__(self, n2):
        return self.n1 + n2.n1
        
n = Number(1)
m = Number(2)

print(n + m)
