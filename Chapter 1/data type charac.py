
# int and bool are immutable and un-iterable but str is immutable but iterable. E:g:-

# Here before there was a object 5 and x was refrencing to it but after wards there is a new object 10 and now x is refrencing to it. object 5 still exsists in memory but as a  garbage. 
x=5
print(id(x)) # some address
x=10
print(id(x)) # different address

# same for bool and str