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

 M=[10,20,30,40,50]
# # for i in M:
# #     print(i)
    
# # how to access the data from list by using the while

# lg=len(M)
# i=0
# while i<lg:
#     print(M[i])
#     i=i+1
    
# How man way we can delete the data from list
# 1. pop()
# 2.remove()
# 3.clear()
# 4.del    
 
 # 1. pop() 
#  -> it remove data by default from last 
#  -> this method is used for delete the data from list by indexing 
#syntax :-
# m.pop(index_number)

# it will delete one data at a time
#  it will return the delete data 


# m=[10,20,30,40,50]
# v=m.pop() 
# print(m)
# print(m.pop()) # remove kiya hua data dikhata h
# print(v)


# m=[
# m.pop(1) # remove by using index
# print(m)



# 2.remove()
# this method is used for delete the data from list
# it will delete specific data from list based on value
# ye return value nhi deta 
# ye do value ko nhi delete krta h : it can delete one data at a time

# m=["mohan","sohan","rohan","chaman"]
# m.remove("rohan")
# print(m)

# abc=[100,200,300,400,500]
# abc.remove(300)
# print(abc)

# syntax:
# abc.remove(list_element)

#  3.clear()
abc=[100,200,300,400,500]
abc.clear()
print(abc)
# list_name.clear():- it will remove all list element

# 4. del :- it will remove the list from memory

# abc=[100,200,300,400,500]
# del abc
# print(abc)


# predefined method in list
# 1. len():- find the lenght of list
# 2. reverse():- it will reverse the list
# 3. sort() :- it will sort in ascending order, for descending sort(reverse=True)
# 4. min() :- it will find the minimum value from list ( only applicable for integer)
# 5. max() :- it will find the maximum value from list
# 6. sum() :- it will find the sum of list element
# 7. count() :- it will count the repeated list element

# 2. reverse():-
# abc=[11,2,4,5,6,7,3,112,99]
# print(abc[::-1]) # slice se reverse
# abc.reverse()
# print(abc)

# # 3. sort() :-
# abc.sort()
# print(abc) # Ascending order

# abc.sort(reverse=True)
# print(abc) # Descending order

# 6. sum() :-
# print(sum(abc))

# print(max(abc))

# print(min(abc))

# print(abc.count(2))


#  # wap to find the min & max value from a given list 
 
# list=[1,2,60,3,50,60]

# # print(min(list))
# # print(max(list))

# m=[10,2,3,4,8,5,218,300,5,500]
# max_value=m[0]
# min_value=m[0]

# for v in m:
#     if v>max_value:
#         max_value=v
#     elif v<min_value:
#         min_value=v


# print("Maximum value=",max_value)
# print("minimum value=",min_value)
        

# Nested list :- List inside list is known as Nested list

# m=[[1,2,3,4],10,50,[100,1,12,34],58]

# v=m[3][0]
# print(v)
# print(m[3][0])

# Create the dynamic nested List

# m=[]
# r=int(input("Enter the row "))
# c=int(input("Enter the column "))

# for i in range(r):
#     a=[]
#     for j in range(c):
#         element=int(input("Enter the list Element "))
#         a.append(element)
#     m.append(a)
# print(m)
        
m=[[1,2,30,4],10,50,[100,1,12,34],158]
mx_value=0
for i in m:
        if type(i)==type([]):
            for j in i:
                if j>mx_value:
                    mx_value=j
        else:
            if i>mx_value:
                mx_value=i
                
print("Maximum value= ",mx_value)
            

#  Wap to remove the duplicate value from list without using predefined & find the count of differennt value present in list

# m=[10,2,1,0,1,0,1,0,1,4,2,0,1,0,1,0,10,1,0,10]
# r=[]

# for i in m:
#     if i not in r:
#         r.append(i)
        
# print(r)
# print("number of different value in list=",len(r)) # c=0 and c=c+1 wala se bhi ho sakta h 

# WAP to find the maximum no of repetition and its elements
my=[10,2,1,0,1,0,1,0,1,4,2,0,1,0,1,0,10,1,0,10,10,10,10,10,10,10,10,10,0,0,0,0,0,0,]
e=0
m=0
# print(set(m))
for i in set(my):
    c=my.count(i)
    if c>m:
        m=c
        e=i
print("Maximum repetition=",m)
print("elements",e)
        
    

#  List compreshension :-
#  it is easy and compact of creating list object from any iterable object
#  list_name=[expression for lv EDT]

# abc=[]
# for i in range(1,101):
#     v=i**2
#     abc.append(v)
# print(abc)

# m=[a**2 for a in range(1,101)]
# print(m)

# m1=[i for i in range(1,101) if i%2==0]
# print(m1)

        
    
