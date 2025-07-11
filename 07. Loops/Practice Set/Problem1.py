# Write a program to print multiplication table of a given number using for loop

start_number = int(input('Number: '))
stop_number = ( start_number * 10 ) + 1
skip_size = start_number

for i in range(start_number, stop_number, skip_size):
    print(i)
