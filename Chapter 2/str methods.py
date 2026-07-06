#                                               Built-in functions

name='Rumman'
# 1) type() -> shows type of variable
print(type(name))

# 2) str() -> converts variable to string
age=21
print("Your age is: "+ str(age))

#                                                 Maths functions

#1) len() -> returns len of variable
print(len(name))

#2) count() -> returns a specific count a sub string in string
print(name.count('m'))

#                                               Transformations

#1) split() -> breaks into lists -> used for extracting the info into lists

data='Adam-24-USA'
print(data.split('-')) # the thing on which we spilt is not included in output.

# 2) repetition (*) -> repeats a string
str='1'
print(str*2)

# 3) indexing and slicing
# they both are used for data extraction
text='python'

# indexing -> extracts only one charcter
print(text[0])
print(text[-1])

# slicing -> extracts series of characters its syntax is:-
# [start:stop:step] -> in this last one (stop,step) is not included that if 6 that means 5

print(text[0:6])
print(text[0:6:2])
print(text[::-1])

date='2026-09-20'
print(date[0:4])

# 4) f-String
is_student=True

print(f"My name is {name} and my age is {age} and student status is {is_student}")

# without f-string we had to add all varible and convert them to str

print(f'2+3={2+3}')
print(f'{{This is me}}') # for string use double brackets {{}}

# 6) Concatination
folder="C:\\USERS\\PYTHON\\"
file="str.py"

full_path=folder+file
print(full_path)

# 7) replace() -> can replace a thing with another or rreplace it via spcae
price='123,45'
print(price.replace(',','.'))
price2=123.45
print(price.replace(',',''))

# challange
number="+49 (176) 123-4567"
print(number.replace('+',"00").replace('(',"").replace(')',"").replace(" ","").replace('-',''))

#                                                 Cleaning
# 1) cleaning things from left and right
# strip can clean/remove anything from left and right but not from middle
text=' Engineering '
print(text.strip())

text=' Engineering'
print(text.lstrip())

text='Engineering '
print(text.rstrip())

text1='###ABC###'
print(text1.strip('#'))

# join -> converts the list back into string
words = ["Python", "is", "awesome"]

result = " ".join(words) # join with space
print(result)

fruits = ["Apple", "Banana", "Mango"]

result = ", ".join(fruits) # join with comma
print(result)

# for checking white space in a huge dataset

text3=" Computer"
print(len(text3)==len(text3.strip()))
# if False they  are not equal it means data has white spaces

# 2)                                           case conversion
# lower()
company="Usol"
print(company.lower())
print(company.upper())

# if we want to search a word in a huge data set we can search it by cleaning white spaces and making it lower:-
company1='Devsinc'.lower().strip()
company2='devsinc'.lower().strip()
print(company1==company2)

# challenge
string='968-Maria, (D@t@ Engineer) ;; 27y  '
string=string.replace(';',',').split(',')
string=string[0:2]+string[3:]
string[0]=string[0][4:]
string[1]=string[1].replace("@",'a').replace('(',"").replace(")","").lower().strip()
string[2]=string[2].replace("y","").strip()
name=string[0]
role=string[1]
age=string[2]
print(f'name: {name} | role: {role} | age: {age}')

#                                             Search

# 1) startswith() -> starts counting from start and returns True if found

# here we can check the valid phone numbers
phone="+923120542234"
print(phone.startswith('+92'))

# here we can check the  email valid domains
email='mkz2003@gmail.com'
print(email.endswith('@gmail.com'))

# here we can check the file types
file_type="file.csv"
print(file_type.endswith('.csv'))

# 2) in -> checks if specific words is in a string

# here we can check wether url is an api call
url='https://api.company.com/v1/data'
print("/api" in url)

# 3) find()

phone1="+92-3120542234"
phone2="92-3120542234"
phone2="0092-3120542234"

# by this we can extract phone numbers no matter if we have  '+' or not.
print(phone1[phone1.find('-')+1:])

#                                              Validation

# 1) isalpha()
country="USA"
print(country.isalpha())

# 2) isnumeric() -> only works if pure numbers not with '-' and decimal points

code='123'
print(code.isnumeric())

# 3) isalnum()
code1='123a'
print(code.isalnum())

# 4) isdigit()
# 5) islower()
# 6) isupper()
# 7) isspace()
code2='123 45'
print(code2.isspace()) # works if only has space