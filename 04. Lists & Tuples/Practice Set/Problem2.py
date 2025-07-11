# Accept marks of 6 Students and display them in a sorted manner
print('\nEnter marks of 6 Students..')

s1 = int(input('\nStudent1 Marks: '))
s2 = int(input('Student2 Marks: '))
s3 = int(input('Student3 Marks: '))
s4 = int(input('Student4 Marks: '))
s5 = int(input('Student5 Marks: '))
s6 = int(input('Student6 Marks: '))

Marks = [s1, s2, s3, s4, s5, s6]
Marks.sort()

print(f'\nSorted Marks of Students: \n\t{Marks}\n')
