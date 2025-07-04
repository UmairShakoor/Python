print('\n\'Computer Student\'s Grade Book\'\n') # Project Name

print('Creating a record of Student\'s Marks then you can search...\n') # Process Info

student1 = input('Student Name: ').capitalize() # Student1 name with first letter capital
std1_marks = input(f'Marks of {student1} : ' ) # Marks of Student1

student2 = input('\nStudent Name: ').capitalize()
std2_marks = input(f'Marks of {student2} : ')

student3 = input('\nStudent Name: ').capitalize()
std3_marks = input(f'Marks of {student3}: ')

marks = {
   student1: std1_marks,
   student2: std2_marks,
   student3: std3_marks
}

print('\nCongrats!, Record Book successfuly created') # Process Completed

search_std = input('\nSearch any Student Marks: ').capitalize() # Make search student capitalized to avoid case issue in search results

if search_std in marks: # Checks if search student present in marks
    print(f'\nMarks of {search_std} are: {marks.get(search_std)}\n') # Print Marks of search student

else: # if not present
    print(f'\n{search_std} not present in Record\n') # Gives record incomplete
