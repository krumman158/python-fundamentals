#                                                List
# List are ordered, allows duplicates, indexed i:e we can access items by their indexes and they are mutabale.
l1=[10,20,30,10]
print(l1) # ordered # allow duplicates
print(l1[1]) # indexed
l1[3]=30 # mutable
print(l1)

#                                                Tuple 
# Tuples are ordered, allows duplicates, indexed and non-mutable.
tup=(10,20,30,10)
print(tup) # odered, allow duplicates
print(tup[1]) # indexed
tup[1]=30 # error - non mutable
print(tup)

#                                                  Set
# Sets are un-odered , not allows duplicates , not indexed and mutable.
sets={10,20,30,10}
print(sets) # unordered , not allow duplicates
print(sets[1]) # error not indexed
sets.remove(20) # mutable

#                                                Dictionary
# Dictionaries are ordered , keys must be unique but values allows duplicates , keys can be accessed by their names only not by indexes and they are mutable.

mu_dict={'a':10,'b':20,'c':30,'d':30}
print(mu_dict) # odered , only values can be duplicates
print(mu_dict['a']) # access via key names
mu_dict['a']=40 # mutable
print(mu_dict)