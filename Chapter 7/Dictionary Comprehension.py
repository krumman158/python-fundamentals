# Syntax:
# dict={
#         1) Expression
#         2) Loop
#         3) Filter
#                }

# challange: keep only string values and convert them to uppercase

user={'id':1,"name":'John','age':30,'city':'Berlin'}
user_str={
       # Expression
       k:v.upper()
       # Loop
       for k,v in user.items()
       # Filter
       if isinstance(v,str)
}
print(user_str)