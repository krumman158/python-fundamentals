#                                                   Iterators

# Iterators are the process or machine that do our required work.
# we need iterators beacuse 1) for looping over objects 2) for saving memory so we don't have to load all data at once in memory 3) to build efficient pipelines. We can build them via enumerate , map , zip and chain etc. These functions build the custom iterators but they don't let you build them from scartch.

# iterator is a object that helps us to loop over but iterable is the object that has sequence of items e:g strings

# enumerate -> a iterator that returns value with its index. We can use it to find bad data (null or empty) in our datasets.
let=['a','b','c','']
for index,value in enumerate(let,start=1): # we can give our own numbering (1) instead of 0
    print(index,value)

student = {"name": "Ali", "age": 20, "city": "Lahore"}
for index, (key, value) in enumerate(student.items()):
    print(index, key, value)

# zip -> same as enumerate it is also an iterator. We can sue it map one data's item to another.
letters=['a','b','c']
numbers=[1,2,3]
for l,n in zip(letters,numbers):
    print(l,n)

# map -> we use it to map an object with a function
names=[' Maria ',' John ', ' Kumar ']
print(list(map(str.strip,names)))
for n in map(str.strip,names):
    print(n)

# filter -> we can use it to filter the items in our data according to our requirements. it filters the false value automatically.

l1=['a','','b',None,'c',False]
print(list(filter(None,l1)))

items=['sql','123','python','42']
print(list(filter(str.isdigit,items))) # if only want digits in my data
