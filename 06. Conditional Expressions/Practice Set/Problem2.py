'''  Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user '''

print('\n\tPass or Fail ??\n') # Project Name

total_marks_each = int(input('Total Marks of each subject: '))

eng_percentage = ( int(input('\nEnglish Marks: ')) / total_marks_each ) * 100
urdu_percentage = ( int(input('Urdu Marks: ')) / total_marks_each ) * 100
comp_percentage = ( int(input('Computer Marks: ')) / total_marks_each ) * 100

least_percentage = 33

if eng_percentage <= least_percentage:
    print('\nYou Failed in English')

else:
    print(f'\nYou Passed in English securing {eng_percentage} %')

if urdu_percentage <= least_percentage:
    print('\nYou Failed in Urdu')

else:
    print(f'\nYou Passed in Urdu securing {urdu_percentage} %')

if comp_percentage <= least_percentage:
    print('\nYou Failed in Computer\n')

else:
    print(f'\nYou Passed in Computer securing {comp_percentage} %')

overall_percentage_required = 40
overall_percentage = ( ( eng_percentage + urdu_percentage + comp_percentage ) / ( total_marks_each * 3 ) ) * 100

if overall_percentage < 40:
    print('\nYou Fallen short of required overall percentage. Failed!\n')

else:
    print(f'\nPassed Overall securing {overall_percentage} %\n')
