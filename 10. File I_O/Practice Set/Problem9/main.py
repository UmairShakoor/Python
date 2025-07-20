# Write a program to find out whether a file is identical & matches the content of another file

file = 'origin.txt'
with open(file, 'r') as f:
    f_cont = (f.read().replace(' ','')).lower()

c_file = 'c_origin.txt'
with open(c_file, 'r') as c_f:
    c_f_cont = (c_f.read().replace(' ','')).lower()
    
    if c_f_cont == f_cont:
        copy = True
        
    else:
        copy = False

if copy:
    print(f"'{file}' is identical to '{c_file}'")

else:
    print(f"'{file}' is not identical to '{c_file}'")
    
