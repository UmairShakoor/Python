# Set is a  Collection of well-defined different objects(values etc..) and they are unordered (The order you give to set, it will not remain in that order)

s = {1, 35, 69, 5, 5, 7, 5} # <class 'set'> # No repitition allowed in sets if you do so set will take only one value of that

e = set() # Empty set # Don't use s = {} as it will create an empty dictionary}

# set checks value either equal or unequal to dis-repeat them by using '==' and 'Is their hash value equal'
# So, set consider 3 == 3.0 as same value , though 3 is 'int' and 3.0 is 'float'

# set() only takes one argument

# A set couldn't contain a list because it is not-hashable but we can use `set([])` to add a list inside []

# Sets are mainly used for lightning fast unqiue data gathering without any complex logic
