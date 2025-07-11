print('\n\'Computer Student\'s Grade Book\'\n') # Project Name
print('Creating a record of Student\'s Marks...\n') # Process Info

# Students Input
while True:
    students = input('How many students record you want to create: ').replace(' ','')

    if not(students.isdigit()):
        print('Input Invalid. Enter a number')
        continue

    students = int(students)
    break

record = {}
total_marks_list = {}

# Student Name & Marks Input
for i in range(0, students):

    while True:
        student = (input('\nStudent: ').strip()).title()

        if student.isdigit() or student < '0':
            print('Invalid Student Name')
            continue

        break

    while True:
       total_marks = input('Total Marks: ').replace(' ','')

       if not(total_marks.isdigit()) or total_marks < '0':
            print('Total Marks Invalid')
            continue

       total_marks = int(total_marks)

       break

    while True:
        obtained_marks = input('Obtained Marks: ').replace(' ','')

        if not(obtained_marks.isdigit()) or obtained_marks < '0' or int(obtained_marks) > total_marks:
            print('Obtained Marks Invalid')
            continue

        else:
            obtained_marks = int(obtained_marks)
            record.update({student: obtained_marks})
            total_marks_list.update({student: total_marks})

        break

print('\nCongrats!, Record Book successfuly created\n') # Process Completed

# Grades Printing
print('Announcing Result!!\n')

for student, obtained_marks in record.items():
    percentage = ( obtained_marks/total_marks_list.get(student) ) * 100

    if percentage <= 100 and percentage >= 90:
        grade = 'A+'
        grade_desc = 'Outstanding'

    elif percentage < 90 and percentage >= 70:
        grade = 'A'
        grade_desc = 'Excellent'

    elif percentage < 70 and percentage >= 60:
        grade = 'B'
        grade_desc = 'Very Good'

    elif percentage < 60 and percentage >= 50:
        grade = 'C'
        grade_desc = 'Good'

    elif percentage < 50 and percentage >= 40:
        grade = 'D'
        grade_desc = 'Fair'

    elif percentage < 40 and percentage >= 0:
        grade = 'F'
        grade_desc = 'Very Bad'

    else:
        grade = 'Unkown'
        grade_desc = 'Error'

    print(f'Grade of {student} is: {grade} ({grade_desc})\n')

# Removing Student
wanna_remove_student = (input('Do you want to remove a student from record? (y/n): ').replace(' ','')).lower()

if wanna_remove_student == 'y' or wanna_remove_student == 'yes':
    remove_student = (input('Enter Student Name you want to remove: ').strip()).title()

    print('')
    if remove_student in record:
        record.pop(remove_student)
        print(remove_student, 'Removed from record\n')

    else:
        print(remove_student, 'Not Found!\n')

else:
    print('Good Bye\n')

