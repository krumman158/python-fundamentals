#                                                Values
# There are only two values True and Values

#                                               Functions
# 1) Bool()
x=123
print(bool(x))
 
y=None
print(bool(y))

z=0
print(bool(z)) # zero and empty and none all are false
print(bool("")) # False
print(bool()) # False

# 2) any() -> checks if any  of variable is True returns true
email=""
phone=12345
username=""
print(any([email,phone,username]))

# 3) all() -> checks if all variables are True then only returns true

email="hiihi"
phone=12345
username="dfdg"
print(all([email,phone,username]))

# can use all and any for input validations in our website or apps

#                                    Comparision operators
# They are used to compare two values
# ==,>,<,>=,<=,!=

#                                     Logical Operators
# and , or , not

print(5==5 or 8>5 and 6<4) # it works by checking the precedence as True has higher than False
# it works as 5==5 or 8>5 -> True then 8>5 and 6<4 -> False so from true and false , true is selected

# challange -> the user can be guest or can be logged in but must  not be banned
is_logged_in=True
is_guest=False
is_banned=True

print(is_logged_in or is_guest and (not is_banned))# here is_banned is True but we isbanned to be False so we use not


#                                            membership operators
# in , not in
# we can use this as we make a list of banned domains of our company and check wether the user's domain is banned or not

print('a' in 'Data') # True
print('a' not in 'Data') # False

#                                              identity operators
# is, isnot
# is checks i:e if two variables point to same object also their object id

a=[1,2,3]
b=[1,2,3]
print(a==b) # True because a and b has same values
print(a is b) # False because a and b has different object ids

a1=5
b1=5
print(a1==b1) # True because a and b has same values
print(a1 is b1) # True because a and b has small value so python puts both of  

# challange
# 1) check if user's name is not empty and age is greater than or equal to 18

name='Rumman'
age=21
print(name is not None and name!="" and age>=18)

# 2) check if password is atleast 8 character long and does not contain spaces

password=1234
print(len(str(password)) >=8 and " " not in password)

# 3) check if user's email is not empty, contain@ and ends with .com

email="rumman@gmail.com"
print(email!="" and '@' in email and email.endswith('.com'))

# 4) check if username is a string and is not none and is not longer than 5 characters

username='Rumman'
print(username==str(username) and username is not None and len(str(username))<=5)

# 5) check if user is either an admin or a moderator. either not banned or they hev verified email

is_admin=False
is_moderator=True
is_banned=True
is_verfied=True
print((is_admin or is_moderator) and (is_banned or is_verfied)) 