 # Dictionary
# ->  this is a non primitive data types
# that store data in key value pair 
# it is created by using {}
# examples:-
v={"name":"firdous"}
# key should be unique
# value are similar and unique
#  dictionary is mutable in nature
# it does not support indexing and does not support slicing
# order does not preserved

# How to create dictionary

# data={
#     "myimg":"f/my.jpg",
#     "marks":100,
#     "age":[10,20,25,30,80]
# }
# print(type(data))

#  value can be homogenous and heterogenous

# d=dict(key=value)
# v=dict(name="md")
# print(v)
# print(type(v))

# d={1:100,"grad":"A+",2:100,1:500}
# print(d)
# if key are similar it will not through error 
# it will consider last value of dictionary

d={
    47202:{
        "name":"md firdous",
        "branch":"cse",
        "semester":"3rd",
        "pass":"no"
    },
    394:{
        "name":"md bro",
        "branch":"cse A",
         "semester":"4rd",
         "pass":"yes" 
    },
    "enrollment":{
        "name":"md",
        "branch":"cse B",
        "semester":"5rd"
    },
    "fee":[100,200,300,20,10],
    "palace":"bhopal"
}
# v=d["palace"]
# print(v)
# m=[100,200,300]
# print(m[0])
# dd={"name":"mogit"}
# print(dd["name"])

# g=d["enrollment"]
# print(g)

# v=d[39409]
# print(v)
# print(v["name"])
# print(v["pass"])
# print(d[47202])
# g=d[47202]
# print(g["pass"])

# print(d[47202]["name"])
# print(d[47202]["pass"])

# d={
#     "name":"mohan",
#     "age":20,
#     "marks":88,
#     "branch":"cse",
#     "palace":"bhopal"
# }

# how to access data 
# 1. [] :- single value
# 2.  .keys() :- it will print only key inside list
# 3.  .values() :- it will print only value inside list
# 4.  .items() :- it will print both key-value
# syntax: 
# dict_name["key"]
# print(d["age"])
# print(d["name"])


# print(d.keys())
# print(d.values())

# d={
#     "name":"mohan",
#     "age":20,
#     "marks":88,
#     "branch":"cse",
#     "palace":"bhopal"
# }

# # for i in d:
# #     print(i)
# v=d.keys()
# for i in v:
#     print(i, "=",d[i])


# how to delete data from dictionary
# my_dict={"name":"mohan","age":20,"marks":100}
# 1.pop(): it will  delete the specific key from dictionary
#  it will return the deleted value
# it will delete only one value at time
# if key will not exit then it will through the error
# 2.clear(): 
# 3.del
# 4.popitem()
# print(my_dict.pop("marks"))
# print(my_dict)



# my_dict={"name":"mohan","age":20,"marks":100,"fee":10}
# popitem: it will remove and retuen the last key value pair data from the list
# v=my_dict.popitem()
# print(v)
# print(my_dict)


# zip():it is used to combine the key and value or two list in one dictionary
# it is used convert list  into dictionary
# name=["mohan","mayank","md","aman","jafar","om","dablu"]
# roll_no=[1,2,3,4,5,6,7]
# d=dict(zip(name,roll_no))
# print(d)


# name=("mohan","mayank","md","aman","jafar","om","dablu")
# roll_no=(1,2,3,4,5,6,7)
# d=dict(zip(name,roll_no))
# print(d)


# wap to take dict from the keyboard and print the sum of value from a dictionary
d=eval(input("enter the dictionary"))  # {'a':10,'b':20}
v=d.values()
print(v)
res=sum(d.values())
print(res)
# a,b,c,=list(int(input("enter the number")).spilt()

# topper={"mohan":20,"sohan":50,"sita":45}
# v1topper.item()
# print(type(v1))
# print(v1)
# v=topper.values()
# print(max(v))
