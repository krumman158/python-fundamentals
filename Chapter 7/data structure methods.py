#                                           Set Methods
# add(x)	Adds one element
# update(iterable)	Adds multiple elements
# remove(x)	Removes element (error if not found)
# discard(x)	Removes element (no error if not found)
# pop()	Removes and returns a random element
# clear()	Removes all elements
# copy()	Returns a shallow copy
# union()	Returns union of sets
# intersection()	Returns common elements
# difference()	Returns elements in first set only

#                                         Tuple Methods
# count(x)	Counts occurrences
# index(x)	Returns first index of element

#                                         Dictionary Methods
# clear()	Removes all items
# copy()	Returns shallow copy
# fromkeys(iterable, value)	Creates new dictionary
# get(key)	Returns value safely
# items()	Returns key-value pairs
# keys()	Returns all keys
# values()	Returns all values
# pop(key)	Removes specified key
# popitem()	Removes last inserted item

#                                     Built-in Methods of All 3
# len()	 works on All 3
# max()	 works on All 3 (dictionary uses keys)
# min()	 works on All 3 (dictionary uses keys)
# sum()	Sets, tuples (numeric values)
# sorted()	works on All 3
# any()	    works on All 3
# all()	    works on All 3
# type()	works on All 3
# enumerate()	works on All 3
# reversed()	Tuples (and other reversible sequences)
# list()	Converts to list
# tuple()	Converts to tuple
# set()	    Converts to set
# dict()	Creates dictionary

#                         Use Cases
# Use a set when:
# Duplicate values are not allowed.
# You need fast in checks.
# You need set operations like union or intersection.

# Use a tuple when:
# The values should stay the same.
# You want to group related values.
# The data shouldn't be modified accidentally.

# Use a dictionary when:
# Every value has a unique key.
# You need fast lookups by name or ID.
# You want to associate related information.