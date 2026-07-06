#                                               Lambda

# we use lambda for shorthand functions instead for building whole functions we can build one line functions
# syntax 1) Lambda keyword 2) any variable x: 3)  what we have to do for that variable

multiply=lambda x: x*x
print(multiply(2))

add=lambda x,y: x+y
print(add(1,2))

# lambda with map
prices=['$12.5','$14.5','$17.5']
print(list(map(lambda p:p.replace("$",""),prices)))

# lambda with filter
prices2=[120,30,300,80]
print(list(filter(lambda p: p>=100,prices2)))

# lambda with nested lists
students=[ ['Maria',85],
           ['Kumar',90],
           ['Max',69] ]
print(list(filter(lambda row: row[1]>=70,students)))

sort=lambda row:str(row[0]).startswith('M')
print(list(filter(sort,students)))
