# f = open('file.txt')
# print(f.read)
# f.close()

# The same thing can be done using with statement like this:

with open('file.txt') as f:
    print(f.read())

# you don't have to write f.close()
