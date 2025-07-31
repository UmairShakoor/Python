# Write a list comprehension to print a list which contains the multiplication table of a user entered number

while True:
    try:
        n = int(input('\nNumber: ').strip())
        break
        
    except Exception as e:
        print('Invalid Number')
        continue

mul = [n*i for i in range(1, 11)]

print(mul)
