from functools import reduce

# Map Example
l = [1, 2, 3, 4, 5]
square = lambda x: x*x

sq_list = map(square, l) # Map is used to run a function on all the elements of a list...
print(list(sq_list))

# Filter Example
def even(n):
    if n%2 == 0:
        return True
    return False

onlyEven = filter(even, l) # Filters Out specific values (elements) from list
print(list(onlyEven))

# Reduce Example
sum = lambda a,b : a+b
print(reduce(sum, l)) # Iterates list and applies a specific function on both values one by one ...
