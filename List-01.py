           #    list 

# 1.non promitive data tye means we can strore single value , multiple value
#2. by using the [] we can create the list 
# example : m=[]
# 3.we can store multiple value with separeted by ,
# ex: m=[10,20,40,50]
# 4.list can store homogenous(same data type) and heterogenous(different data type) data type value
# exaple: m=[10,20,30,40]  -> Homogenous
# example: n=["skill",10,20,30.5,True] -> Heterogenous
# 5. list allow duplicates value 
# example m=[10,10,10,10] m=["job","job"]
# 6. list support indexing 
# ex: ,=[100,200,300]
# list support both positive and negative indexing 
# left to right index value will be +ve
# right to left then index will be -ve
# m=[100,200,300,400,500]
# print(m[0])
# print(m[4])
# print(m[-1])
# 7.List support slicing (this is a method to access data from list)
# 8. list is mutable in nature (we can modifies (we can add or delete the data )) the list

# ex: 
# m=[100,200]
# print(m)
# m.append(300)
# print(m)
# m.pop()
# print(m)

# how to create list dynamically
# []
# 1 .append()
# 2 .extend()
# 3 .index()
# 4 .list()
# 5 .split()
# 6 .insert()

# how to create the empty list
# m=[]
# print(type(m))
# print(m)

# m=list(input("Enter the number "))
# print(m)
# print(type(m))

# append() :- this method is used for add the dynamic data
# by default append() add the data end of the list  
# append jaisa data dete h waise hi add kr deta h
# this will add as it as data
#  ye lenght ko badha deta h 
# m=[]
# m.append(10)
# m.append(20)
# # for i in range(10):
# #     m.append(i)
# print(m)
# m.append(["mohan","sohan"])
# print(m)

# m.extend(["mayank","rehan"]) # extend() sabko alag alag add krta h 
# print(m)
   
 # indexing():- ye replace krta jisse lenght same rahta h 
#  it will replace old value with new value 
#  it cannot change the lenght of list
# it can add specific data inside list by using index no
m=["skill","coding",100]
# m[0]="degree"
# print(m)
print(len(m))
print("index no=",m.index("coding"))
# this method is used for find index no of list element
m[2]=[100,200,300]
print(m)


