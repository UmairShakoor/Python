# Write a program which finds out whether a given name is present in a list or not

names = ['Umair', 'Shakoor', 'Harry', 'Haris', 'Ali']

find_name = input('Name: ').capitalize()

if find_name in names:
    print(f'{find_name} present')

else:
    print(f'{find_name} not present')
