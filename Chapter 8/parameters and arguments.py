# Parameters are the names used in function definition that describe what data the function expects. They are the placeholders.

# Arguments are the real values passed in a function call that are assigned to parameters. They are the values taht fill the place holders.

#                                              Types of Variables
# 1) Parameters
# 2) Global Variable -> created outside the function and can be accessed anywhere.
# 3) Local Varibale -> created inside the function and can be accessed only inside the function.

# E:g

def greet(name):
    print(f'hello {name}')

greet('Rumman')

# Here name is a local variable after func call finishes local vriable (name) is destroyed from memory.

# 'Rumman' was refrencing to name during func call but after it was not refrencing so python collects it as garbage and may destroy it instantly or shortly afterwards.

# E:g

def greet2(name):
    print(f'hello {name}')

x='Ali'
greet2(x)

# Here name is a local variable after func call finishes local vriable (name) is destroyed from memory.

# X is a global variable and remain in the memory even after func finishes but till the program itself exits.

#                                         Types of arguments

# 1) Positional Arguments -> values passed to the function based on their order.
 
# 2) Keyword Arguments -> values passed to the functions based on their names. 

# E:g 
def data(first_name,last_name,country):
    first=first_name.strip().lower()
    second=last_name.strip().lower()
    full_name=first+" "+second
    print(f'{full_name} from {country}')

# positional arguments but if change the order i:e if i write 'Pakistan' first then my first name will be 'Pakistan'. So order matters here.
data('Rumman','Khan','Pakistan')
data("Pakistan",'Rumman','Khan') # order changed wrong output

# Keyword Arguments. Here order doesnot matters
data(country='Pakistan',first_name='Rumman',last_name='Khan')

#                                           Types of Paramters

# Default Parameters -> parameters that has already a value so if you don't pass anything , python uses that value automatically. Rule-> can be listed after non-default parameters.

# E:g
def data(first_name,last_name,country='n/a'):
    first=first_name.strip().lower()
    second=last_name.strip().lower()
    full_name=first+" "+second
    print(f'{full_name} from {country}')
# uses default value
data('Ali','Ahmed')

#                                               *args **kwargs

# we use it because sometimes we don't know how many arguments will be passed to your function. They allow functions to accept a unknown number of arguments.

# *args   -> Only for positional arguments their type is tuple. Only use when all values have same data type i:e 1,2,3 -> all are int.

# *kwargs -> Only for keyword arguments their type is dictionary. Only use when all values have different data types

# E:g
def total(*args):
    print(sum(args))

total(1,2,3) # i can give as much arguments i want for sum

def user_info(**kwargs):
    print(kwargs)

user_info(first_name='Rumman',last_name='Khan',age=21,country='Pakistan')

#                                               Return 
# For return we always have to store the returned variable otherwise we cannot see it.
# E:g
def name(name):
    clean=name.strip().lower()
    return f"name is {clean}"

cln=name('Rumman')
print(cln)

def mutiple(name):
    lo=name.strip().lower()
    up=name.strip().upper()
    return lo,up

lo_name,up_name=mutiple('Rumman')
print(lo_name)
print(up_name)