# This program prints table of a number entered by the user to 10

print('\n\tMultiplication Table Generator')

number = int(input('\nTable of: '))
end = int(input('Till what number you want the table?: '))

for i in range(1, end + 1):
    print('')
    print(f'{number} X {i} = {number * i}')

print('')
