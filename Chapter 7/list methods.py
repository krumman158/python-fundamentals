#                                              Built-in Functions
# max,min,len,sum
numbers=[1,2,3,4,5]
print("Max: ",max(numbers))
print("Min: ",min(numbers))
print("Len: ",len(numbers))
print("Sum: ",sum(numbers))

# all -> returns True when all values are true/real. returns false when any value is none, missing, empty and false
num2=[1,0,0]
print("All: ",all(num2))

# all -> returns False when all values are false. returns True when any value is true/real
print("Any: ",any(num2))

#                                                  Methods

# count -> returns how many times a items exists in a list
print("Count of 5: ",numbers.count(5))

# index -> returns the index of a item in a list
print("Index of 5: ",numbers.index(5))

#                                                 Operators

# in -> checks if a item exists in a list and returns true/flase
print(4 in  numbers)

# == , > , < but > and < compare only first and last items

#                                               Adding Lists methods

# append -> adds item at end of list
numbers.append(7)
print(numbers)

# insert -> adds item in list ata specific location. Locations start from 0....
numbers.insert(5,6)
print(numbers)

# extend -> it extends list without adding a new list

numbers.extend([8,9,10])
print(numbers)

#                                                   Removing

# clear -> make list empty
num2.clear()
print(num2)

# remove -> removes items that first matches the given value in remove()
num3=[0,1,0]
num3.remove(0)
print(num3)

# pop -> removes items whose index is given in pop() but is no index is given it by default removes the last item. It always returns the removes value
letters = ['a','b','c']
removed = letters.pop(0) # we store the removed value in removed
print(letters,removed)

# pop vs remove -> pop() removes by index , also returns the poped value and remove() removes by value, returns nothing


#                                                    Updating

letter=['a','b','c']
letter[0],letter[1],letter[2]='x','y','z'
print(letter)


#                                                    Sorting

# sort() -> oders the list in ascending order but when sort(reverse=True) it oders in descending
letter.sort()
print(letter)
letter.sort(reverse=True)
print(letter)

# sorted() -> it makes copy of original list and copy is sorted and it doesnot changes the original list 

let=['c','a','b']
new_list=sorted(let)
print("Original List: ",let) # unchanged
print("Sorted Copy: ",new_list)

new_list2=sorted(let, reverse=True)
print("Original List: ",let) # unchanged
print("Sorted Copy: ",new_list2)

#                                                  Reversing

# reverse -> changes the position of first and last items in the original list
rlist=[1,5,2,4]
rlist.reverse()
print(rlist)

# reversed() -> same as reverse but don't changes the original list instead makes a copy and returns a iterator not list

reversed_list=reversed(rlist)
print("Original List: ",rlist)
print("Reversed List",reversed_list) # returns a iterateable object
reversed_list=list(reversed(rlist)) 
print("Reversed List",reversed_list) # now returns a list

#                                                Combining

# we can concatenate two lists via + operator can also be done same via extend()
l1=['a','b','c']
l2=[1,2,3]
comb=l1+l2
print(comb)

# we combine two lists in one but as separate group via ','

comb2=[l1,l1]
print(comb2)

# zip -> combines items of first list with second list in order but it returns a iterateable object which is a tuple so we have to convert it to nay datatype. But if any list have more items than other the excesssive items are not zipped. Can be used when info in one list belongs to info in other lists
id=[5017,5018,5024]
names=['Rumman','Rafay','Abdullah']
comb3=list(zip(id,names))
print(comb3)
