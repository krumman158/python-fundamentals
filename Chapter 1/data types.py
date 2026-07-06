# python automatically detects the data types so we not have to mention it like in java or c++
 
a=10 #int
b=3.14 #float
c='sss' #str
d='123' # number but still string
e=True #bool
f=False #bool
g=None # none value means nothing or unknown 
h='' # here it is a blank str not none
i=[1,2,3,4] #list
j=(1,2,3) # tuple
k={1:'number'} #dict
l={1,2,3} # set
 
# challange
age=21 #int
height=172.24 # float
name='Rumman'
Are_you_a_student=True
no=None

print(age,height,name,Are_you_a_student,no)
print(type(age),type(height),type(name),type(Are_you_a_student),type(no))

# len works with str,tuple,set,dict,list,bytes
print(len(name))