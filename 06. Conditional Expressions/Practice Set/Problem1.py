# Write a program to find greatest number in four numbers entered by the user

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))
number4 = int(input('Enter fourth number: '))

numbers_set = {number1, number2, number3, number4}
greatest_number = max(numbers_set)

print(f'Greatest Number is: {greatest_number}')
