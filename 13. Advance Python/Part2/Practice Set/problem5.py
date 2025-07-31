# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1, 2, 3, 5, 7, 9]

max_ = lambda a,b: a if (a>b) else b
print(reduce(max_, l))
