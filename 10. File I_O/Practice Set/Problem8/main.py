# Write a program to make a copy of a text file 'this. txt'

file = 'this.txt'
with open(file, 'r') as f:
    f_cont = f.read()

c_file = 'this(1).txt'
with open(c_file, 'w') as c_f:
    c_f.write(f_cont)
