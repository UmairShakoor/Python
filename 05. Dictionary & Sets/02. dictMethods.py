d = {} # Empty Dictionary # <class 'dict'>

marks = {
   'Harry': 100,
   'Adnan': 99,
   'Ayan': 98,
   '0': 0.00
}

print(marks.items()) # Returns all key-value Pairs of dictionary
print(marks.keys()) # keys of Dict
print(marks.values()) # Values of Keys in Dict

marks.update({'Harry': 99, 'Hello': 'World'}) # Updates the original dict bcz dict are mutable
print(marks)

print(marks.get('Harry2')) # Prints None
# print(marks['Harry2']) # Returns an Error

print(len(marks)) # Gives length of key-value pairs in dict

# marks.clear() # Clears (Make Empty) dict
print(marks)

pop_value = marks.pop('0') # Removes key-value pair from dict and returns its (key's) value
print(pop_value)
print(marks)

popped_item = marks.popitem() # Removes the most-recent (latest) key-value pair from dict and returns that key-value pair
print(popped_item)
print(marks)


