
s = {1, 54, 32, 5, 5, 7, 5, 'Harry'} # Their can be values of different DataTypes in a set
print(s, type(s))

# s.add(566) # Adds one argument at a time
s.update(566, 78, 9)
print(s)

# s.clear() # Clears the Set same as in case of dictionary
# print(s)

# print(s[0]) # Invalid bcz Can't index any data in Sets

print(len(s)) # Gives length of set

s.remove(1) # Removes data
print(s)

s.pop() # Removes random data from set
print(s)


# Union & Intersection

s1 = {1, 45, 6, 79}
s2 = {7, 8, 1, 79}

print(s1.union(s2)) # Prints union of s1 & s2
print(s1.intersection(s2)) # Prints intersection of s1 & s2

