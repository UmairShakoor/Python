a = 89 # Global Var

def fun():
    global a # it changes global variable a
    a = 3 # Local Var
    print(a)

fun()    
print(a)
