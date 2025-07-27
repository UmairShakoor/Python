# Create a class with a class attribute a; create an object from it and set 'a' directly using 'object.a = 0'. Does this change the class attribute?
# Answer: Yes , Explanation:-

class change:
    a = 5

print(change.a)
change.a = 0
print(change.a)
