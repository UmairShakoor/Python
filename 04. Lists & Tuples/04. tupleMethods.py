
a = (1,4,5,"Harry",False, 4, 'World', None)
print(a)

no = a.count(4) # Return total number of occurence of data in a tuple (same as string)
print(no)

firstOccur = a.index(4) # Returns index of first occurence of data
print(firstOccur)

print(len(a)) # Gives length of tuple

numbers = (2, 4, 9, 10)
print(max(numbers)) # Returns the largest value in tuple
print(min(numbers)) # Returns the smallest value in tuple
