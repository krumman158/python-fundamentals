# With help of list comprehension we can do all 3 in one i:e 1) data transformation 2) for loop 3) data filtering 
# Syntax -> list=[
#                 data transformation
#                 loops
#                 data filtering (if required)
#                                    ] 

# task -> remove the things that are not domains
domains=['www.google.com','openai.com','localhost','WWW.DATAWITHBARAA.COM']

cleaned=[

         # data trandfromation
         d.lower().replace('www.','')
         #loop
         for d in domains
         # data filtering
         if '.' in d
]

print(cleaned)