# print ("Enter the number :")
# v=input()
# print ("the value iof v=",v)

# name = input("name:")
# print ("my college name is",name)

# print("name")
# name = input()
# print("my college name is",name)

# n1=input("number1=")
# n2=input("number2=")
# sum=n1+n2
# print ("the sum of number1 and number2 is",sum)


#  imp point:  . input data hamesa string me layega 
# input method is used for get the data from user in string "" format


# name=input("enter the name")
# print("my name is ",name)


# firstname= "md "
# secondname= "firdous"
# fullname= firstname+secondname
# print(fullname)

# n1=int((input("the first no:")))
# n2=int((input("enter the second no:")))
# print(type(n1))
# print(type(n2))
# s=n1+n2
# print("the sum =",s)



# how to know the data type in python

# print(type(n1))
# print(type(n2))


# # get the name from user and print in 1k time ?

# name=input("Enter your name: ")
# print(name*1000)


# write a program to print the power of 2 a given number 

# n1=int(input("enter first no:"))
# n2=int(input("enter second no:"))
# print(n1**2)
# print(n2**2)

# two number n1 and n2 power then sum
n1=int(input("enter first no:"))
n2=int(input("enter second no:"))
# print (n1**2,)
# print (n2**2,)
s = (n1**2) + (n2**2)
print (s)

# name = input("Enter your name :")
# title =input("Enter your title:")
# fullname= (name)+" "+(title)
# print(fullname)


# add two number without using +
# n1=int(input("enter n1"))
# n2=int(input("enter n2"))
# print(sum((n1,n2)))
# print(min((n1,n2)))
# print(max((n1,n2)))

# name=input("Enter your name:")
# age=int(input("enter your age:"))
# branch=input("Enter your branch:")

# print("my name is ",name,","" my age is ",age,"years,","my branch is",branch)

# print(f"my name is {name},my age is {age} years ,my branch is {branch}.")

# print("my name is {0},my age is {1} years ,my branch is {2}.".format(name,age,branch)) # yaha f use nhi karenge


# typecasting = it is a process to convert one data type to another data type
# int() :- this method is used for converting to integer


# method 1
n1 = int(input("enter no 1:-"))
n2 = int (input("enter no 2:-"))
s = n1+n2  # yaha pe bhi hum chahe to direct typecasting kar sakte h
print(s)


# method 2
n1 =(input("enter no 1:-"))
n2 =(input("enter no 2:-"))
s = int(n1)+int(n2) # yaha pe direct typecasting kiye h
print(s)



#  Data type :- type of data is known as data type 
# 1) primitive    2) non- primitive

# 1) primitive
# . it store single value in a varaiable.
# . basic , built in data type
# -> int(10,-10,0)
# -> float(10.0,-11.2,0.0)
# -> str("hi",'hi','''hi''')
# -> bool(True,False)
# -> complex(3+4i)




# 2) non- primitive
# . it store multiple value in a variable.
# . derived data type

# -> rule 
# list a =[] , tuple c = () , set b={}

# 1) list = list is a non primitive data type , by using square bracket[] 
#           we can store homogenous (same datatype) and heterogenous(different datatype) ,
            # we can store multiple value inside list seperated by comma(,)

    #         -5   -4    -3     -2    -1
    #   m = [ 10,'skill',"piza",True, 10.2]
    #          0    1     2      3      4
        # index0  index1  index2 ...........
    # list support indexing both positive and negative 
    # left -> right = index will start from 0
    # right -> left = index will start from -1
    
    
# m= [100,200,"md"]
# print(m[2])
# print(m[-1])

a=[10,30,20]
a[1]=20
print(a)   # mutable h replace ho rha h 



# tuple :- it is same as list , but immutable = na hi add/delete ya replace kr sakte h 


# by using the parentheses () we can create the tuple 
# () is optional

# a=(10)  # integer a = 10 
# print(type(a))
# b = 10 # int
# b = 10,  # check , for tuple.
# print(type(b))
# c = (100,200,300)
# print(type(c))
# c = 100,200,300
# print(type(c))

# d=100,"md"
# print(d[1])

d=(10,10,10,10,'md')
print(d)  # duplicate value support

# a=(10,20,30)
# a[0]=22      # error de rha = immutable


# set {}
# set support homogenous and heterogenous data type
# set does not support duplicate value 
# set does not support indexing q ki random value (duplicate value) ko hatata h 
# v = {10,10,10,10,10,10,20,"skill"}
# print(v)

s={1,2,3}
s.add(4)
print(s)  # add/delete kr sakte h = mutable


#              non-primitive d.t
#  list             tuple      set
 

#  index             ,,        not
#  homo,hetero        ,,        ,,
#  []                ()         {}
#  duplicate          ,,      not
#  mutable       immutable     mutable



#  Dictionary 
# by using {} we can create the dictionary
# it always store value in key_value pairs
# d= {"name":"md firdous","branch":"cse"}



#how to know the data type in python
a=10
b=20
c=0
print(type(a))
print(type(b))
print(type(c))

a=10.8
b=20.8
c=0.0
print(type(a))
print(type(b))
print(type(c))

s="md"
print(type(s))
v=100
print(type(v))
v3="""333.6"""
print(type(v3))

ab_c=True
abc=False
print(type(ab_c))
print(type(abc))

# a=true # error dega q ki koi bhi data type nhi h
# print(type(a))

a=3+5j
print(type(a))


# # type casting
# int() :- 
# float()
# str()
# bool()
# complex()
# list()
# tuple()
# set()
# dict()
# range()
# bin()
# oct()
# hex()

# # int() :- this method is used for convert any data type to integer
# a = 10.3
# a=10.3
# print(int(a))
# # b="md"
# print (int(b))  # error

# note: if string value is int then it will convert in integer
# data type but if string value is charactter then it can not convert

# abc="10.2"
# print(int(abc)) # error q ki sirf integer value ko hi karega but ye float h 

# a=True
# print(int(a))  # output = 1

# b = False
# print(int(b))  # output = 0

 #  note:- all number system (decimal,hexadecimal,binary,octal) is int datatype.
 
#  a=10101010          decimal(10)
#  a=0b10101010         binary(2)
#  a=0o10101010         octal(8)
#  a=0x10101010         hexadecimal(16)


# how to covert one number system to another number system

# int() : this method is also used for convert any number system to decimal number system

# a=101010       # decimal to decimal isiliye same aaayega
# print(int(a))

# a=0b1010     # binary number 0b
# print(int(a))

# c=0o101010   # octal number 0o
# print(int(c))

# b=0x1010     #hexadecimal number 0x 
# print(int(b))

# # bin() : this method is used for convert any number system  to binary number  sysytem

# a=101010
# b=bin(a)
# print(b)

# a=0o101010
# b=bin(a)
# print(b)

# a=0x101010
# b=bin(a)
# print(b)

# # oct() : this method is used for convert the any number system to octal system

# a=101010
# b=oct(a)
# print(b)

# a=0b101010
# b=oct(a)
# print(b)

# a=0x101010
# b=oct(a)
# print(b)


# # hex() : this method is used for convert the any number system to hexadecimal 

# a=101010
# b=hex(a)
# print(b)

# a=0b101010
# b=hex(a)
# print(b)

# a=0o101010
# b=hex(a)
# print(b)

# ** float method : this method used for convert any data type into float except string

# a = 1000
# print(float(a))

a = "1000.7"
print(float(a))

# Note: if the string value is integer & decimal then it will convert into float 

# *** bool(): this method is used for convert the any data type to boolean data types.

# a=1
# print(bool(a))
# b=0
# print(bool(b))

# c ="md"
# print(bool(c))


# *****  NOTE :- it is used to convert all datatype to bool data type 
#   there is no exception it convert string , int , float

# complex 

# n=6
# print(complex(n))









