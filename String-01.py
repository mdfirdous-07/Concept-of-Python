 # string :- it is a primitive data type 
#   Strings is a squence of character
#  that is include with '' , " " or """ """
#  it is immutable in nature 
#  it store data on index
#  string support both -ve and +ve indexing

# s='''
# hi 
# hello
# tata '''   # this is used for writing multiline using tripple quatation
# s="""
# hii 
# hello
# bye"""

# # how to access data from String 
# #  by using the index method
# #  by using for loop
# #  by using while loop
# #  by using slice operator

# # by using slicing
# # a="mdfirdous"
# # print(a[0:9:1])

# # # by using for loop
# # s="my name is md firdous"
# # for i in s:
# #     print(i)
   
# # #  by sing indexing 
# # print(s[0])

# # v=len(a)
# # while v>0:
# #     print(a)
# #     v=v-1

# #  WAP to find the index num with character

# # n="mdfirdous"
# # lg=len(n)
# # i=0
# # while i<lg:
# #     print(f"{i}:{n[i]}")
# #     i=i+1

# #  mathematical operator in string
# # +
# # *
# # ==

# # n1="md"
# # n=" "
# # n2="firdous"
# # s=n1+n+n2
# # print(s)

# s=10+10
# v="10"+"10"
# print(s)
# print(v)

# s=10*10
# # v="10"*"10"  # error dega
# print(s)
# s="10"*10
# print(s)

# v="md"
# v1="ba"
# print(v==v1)

# a="skill"
# b="skill"
# print(a==b)

# how to remove space from strings:-

# 1 .strip() :- it will remove space from both side 
# 2 .rstrip() :- it will remove space from right side 
# 3 .lstrip() :- it will remove space from left side 

# s="   hello"
# # print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())   # yaha right strip nhi h isiliye ye same likh dega 

#  searching / finding methos in string

# 1 .find()
# 2 .rfind()
# 3 .index()
# 4 .rindex()

# for forward direction
# find() :- it will find the sub string in forward direction it will return first occurence of main string
# if substring is available then it will give the index value otherwise (not available)  then print false(-1)

# index():- it will return first occurence of sub string within the main string
# if substring is available then it will give the true otherwise it will through error

#  for backward direction 
#  rfind :- it will find the sub string in backward direction it will return first occurence of main string
# if substring is available then it will give the index value otherwise (not available)  then print false(-1)

#  rindex :- it will return first occurence of sub string in backward direction show the main string
# if substring is available then it will give the index otherwise it will through error

# s="skills"
# v=s.index("k")
# print(v)
# # v1=s.index("L")    # ye error dega q ki not found
# # print(v1)

# s="skills"
# v=s.find("k")
# print(v)
# v1=s.find("L")   
# print(v1)

# s="skills"
# v=s.rindex("k")
# print(v)
# v1=s.rindex("L")    # ye error dega q ki not found
# print(v1)

# s="skills"
# v=s.rfind("k")
# print(v)
# v1=s.rfind("L")   
# print(v1)


# changing case of the string

# 1. upper() :- it will convert the lowercase into uppercase
# 2. lower() :- it will convert in lowercase
# 3. swapcase():- it will convert upper to lower and lower to upper case
# 4. title() :- it convert each and every first letter of a string in capital
# 5. capitalize():- it will convert only first letter word of paragraph as capital

# n=input("Enter the string")
# print(n.lower())
# print(n.upper())
# print(n.swapcase)
# print(n.title())
# print(n.capitalize())

# check the type of character present in a string

# s=input("Enter the character: ")
# isalnum() :- Return True if characters are alphanumeric (a-z , to 0-9)
# isalpha() :- Return True if all character are alphabets (a-z , A-Z)
# islower() :- Return True if all character are in lowercase
# isdigit() :- Return True if all character are digit
# istitle() :- Return True if each word first letter is capital
# isspace() :- Return True if string contain only one space
# isupper() :- Return True if all characters are upper case

# print(s.isalnum())
# print(s.isalpha())
# print(s.islower())
# print(s.isspace())
# print(s.isdigit())
# print(s.isupper())
# print(s.istitle())


# split method
# split method is used to convert string to list with specific delimeter
s="I L U"
v=s.split()
print(v)

#syntax
# s.split(delimeter, no of split)
b="12/03/2003"
print(b.split('/'))
# default delimeter is space
# delimeter can be = , / , @ , % etc

s="skills try sdhk assdk sdfgh hhhjkll"
print(s.split(),3)

# write a program to reverse the given string without using predefined function



# WAP to reverse the order of words
