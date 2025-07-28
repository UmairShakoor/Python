class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o1 = Employee()
o2 = Programmer()
o3 = Manager()

print(o1.a)
# print(o1.b, o1.c) # Shows Error

print(o2.a, o2.b)
# print(o2.c) # Shows Error

print(o3.a, o3.b, o3.c)

