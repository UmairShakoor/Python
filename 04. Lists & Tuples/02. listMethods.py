list = ['Apple', 'Orange', 5, 345.06, False, None]
print(list)

list.append('Harry') # .append() adds data in the end of a list
print(list)

list.reverse() # .reverse() reverse the content of a list
print(list)

numbers = [1,4,5,3,0,2]
# numbers.sort() # .sort() reArranges a list (Works on both Numbers list or Alphabatic list)
# numbers.insert(3, 3333) # .insert(Index, Integer) inserts any integer to a list at a particular index
value = numbers.pop(5) # .pop(Index) is used to delete a character at an index and returns that index value that is popped out
print(value)
print(numbers)

numbers.remove(5) # .remove(value) is used to remove a particular data from a list
print(numbers)
