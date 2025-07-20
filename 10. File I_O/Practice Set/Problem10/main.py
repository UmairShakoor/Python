# Write a program to wipe out the content of a file using python

file = 'empty.txt'
with open(file, 'w') as f:
    f.write('')
