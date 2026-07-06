# we can unpack any data type that is iterateable
st='Hi'
f_st,s_st=st
print(f_st,s_st)

# error breacuse int are not iterateable
# num=12
# f_num,s_num=num
# print(f_num,s_num)

list=[1,2]
f_list,s_list=list
print(f_list,s_list)

tuple=(1,2)
f_tuple,s_tuple=tuple
print(f_tuple,s_tuple)

set={1,2}
f_set,s_set=set
print(f_set,s_set)

# in dictionary only keys are returned in unpacking
dic={1:1,2:2}
f_dic,s_dic=dic
print(f_dic,s_dic)

# we can use _ when want to skip any info while unpacking but it doesnot changes the list
l=['Maria','29','Data Enginner','Spain']
name,_,role,_=l
print(name,role)

# we can use *_ when we want to skip all middle info but it doesnot changes the list
l2=['Maria','29','Data Enginner','Spain']
name2,*_,country=l
print(name2,country)