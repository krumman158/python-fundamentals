#                                                   Copy

# There are two types of copy deep copy and shallow copy. 
# Shallow copy creates a list copy but not at deeper level i:e  copied list is a different object/variable then the original list but adding anything in copy list changes the original list 
# Deep copy creates a list copy but  at deeper level i:e  copied list is a different object/variable then the original list but adding anything in copy list doenot changes the original list. It is created by importing copy module.

matrix=[ ['a','b'],
         
          ['c','d'] ]

matrix_copy=matrix.copy()
matrix_copy[1].append("e")
print("Original: ",matrix)
print("Copy: ",matrix,'\n')  # changes the original matrix also


import copy

matrix2=[ ['a','b'],
         
          ['c','d'] ]

matrix2_copy=copy.deepcopy(matrix2)
matrix2_copy[1].append("e")
matrix2[1].pop()
print("Original: ",matrix2)
print("Copy: ",matrix2_copy)


# shallow , deep copy use case -> use shallow copy for flat list and deep copy for mtrices