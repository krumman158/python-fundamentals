# we can use * to collect all middle info in a list

list=['Maria','29','Data Enginner','Spain']
name,*details,country=list
print(details)

list2=[[1,2,3],[4,5,6],[7,8,9]]
list_one,*list_two,list_three=list2
print(list_two)