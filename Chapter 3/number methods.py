#                                               Types
# 1) type() -> tells the type
x=1
y=3.14
z=3+4j

print(type(x))
print(type(y))
print(type(z))

# 2) convert via int() , float() , complex()
x=3.14
print(type(int(x)))

a=1
b=3
print(complex(a,b))

#                                               Math operators

# +,-,*,/,//,%,**

print(2+3) # adds
print(5-3) # subtracts
print(5*3) # multiplies
print(7/2) # retruns qoutient
print(7//2) # returns the qoutient in int form 
print(7%2) # returns the remainder
print(2**3) # multiplies to the power i:e 2^3

#                                                Rounding
# 1) abs() -> ignores neg sign
print(abs(1-3))

# 2) round() -> rounds off to a specific number
num=3.141414
print(round(num,2)) # rounds off to 2 numbers
print(round(num))

# 3) ceil() -> makes number to the nearest greatest number e:g 35.5 -> 36

import math
print(math.ceil(num))

# 4) floor() -> makes number to the nearest lowest number e:g 35.5 -> 35 
print(math.floor(num)) 

# 5) trunc () -> it doesnot do rounding or ceil or floor it just removes the decimal part same as int()
print(math.trunc(num))

#                                               Advnace Maths 
# sqrt() ,cos() , sin() etc 

#                                                  Random
# we use it to generate dummy data
import random
print(random.random()) # returns a random floating number between 0 and 1

print(random.randint(1,6)) # returns a number from 1 to 6


#                                              Validation
# 1) isinteger()
r=7.1
print(r.is_integer()) # but true for 7.0

# 2) isinstance() -> can be used to check any datatype

print(isinstance(r,int))
print(isinstance(r,float))

name='Rumman'
print(isinstance(name,str))

# challange
number= random.randint(1,100)
print(number)
print('even' if number%2==0 else 'odd')