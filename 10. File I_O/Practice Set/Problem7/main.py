# Write a program to find out the line number where python is present in lines

with open('log.txt', 'r') as f:
    lines = f.readlines()

n = 1
for line in lines:
    if 'python' in line:
        print('Python is present at Line:', n)
        break
    n += 1
else:
    print('Python is not present')
