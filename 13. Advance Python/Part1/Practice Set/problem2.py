# Write a program to print third, fifth and seventh element from a list using enumerate function

l = [0, 1, 2, 3, 4, 5, 6, 7]

for index, item in enumerate(l):
    if (index % 2) != 0 and index != 1:
        print(item)
