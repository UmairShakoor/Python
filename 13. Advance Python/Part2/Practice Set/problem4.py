# Write a program to filter a list of numbers which are divisible by 5.

l = [2, 434, 654, 55, 10, 908, 450]

_5 = lambda n: True if(n%5 == 0) else False
l_5 = list(filter(_5, l))

print(l_5)
