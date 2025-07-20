f = open('file.txt') # read mode is default
# f_cont = f.read() # Reads the whole file
# print(f_cont)

# lines = f.readlines() # Gives list of all lines
# print(lines)

# line1 = f.readline() # Reads first line
# print(line1)

# line2 = f.readline() # Reads next line
# print(line2)

# line3 = f.readline() # Reads next line
# print(line3)

# line4 = f.readline() # Reads next line
# print(line4)

line = f.readline()
while line != '':
    print(line)
    line = f.readline()
f.close()

