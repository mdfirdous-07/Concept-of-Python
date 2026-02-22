 # opertor 
 # operator is a symbolic representation
 # it is used for perform the various operation
 
#  type :-
#  1) arithematic operator
#  2) relational operator : result:- True or False
#  3) logical operator
#  4) assignment operator
#  5) membership operator
#  6) identity operator
#  7) bitwise operator
 
 
#  1) arithematic operator
#  this operator is used for perform the mathematical operation
#  + = addition
#  - = subtraction
#  * = multiplication 
#  % = reminder 
#  // = quotient (bhagfal) integer
#  / = divide
 
# a=input("Enter the number") # 100
# b=input("Enter the number") # 200
# s=a+b
# print(s)  # concenide kr dega 100200
 
# a=int(input("Enter the number")) # 100
# b=int(input("Enter the number")) # 200
# s=a+b
# sub=a-b
# rem=a%b
# divide=a/b
# q=a//b       
# # agar last number ko lana ho to 10 se divide krenge (remender)
# # agar quetient lana rhega to last ko chhor ke aayega
# print(s) 
# print(sub) 
# print(rem) 
# print(divide) 
# print(q) 


# # # 2) relational operator
# # # -> it always apply on operands
# # # -> it give only two result true  and False
# # #     == (Equal operation)
# # #     != (not equal)
# # #     >  (greater)
# # #     < (less)
# # #     >= (greater than =)
# # #     <= (less than =)
    
    
    
    
# # # a = int(input("Enter the number: "))
# # # b = int(input("Enter the number: "))
        
# # # print(a==b)
# # # print(a>b)
# # # print(a<b)
# # # print(a<=b)
# # # print(a>=b)
# # # print(a!=b)

# # s=True   # relational operator apply not on value,not on data type : it compare both value and data type
# # s1='True'
# # print(s==s1)

# # s='True'
# # s1='True'
# # print(s==s1)

# # print(0==0)

# # print(0=='0')



# 3) membership operator 

# # membership operator apply only on eterable data type(EDT).
# # EDT = data inside data

# # membership operator directly we can apply in all non primitive data type .mro
# # it cannot apply directly in primitive data type except string "" .
# #  ( int, float, bool , complex, we can not apply but only apply on string )

# there are two type of membership operator 
# 1, in
# # 2, not in

# # NOTE : it only gives value TRUE and FALSE 


# m="mdfirdous"
# print("m" in m)
# print("d" in m)
# print ("dm" in m )


# # a=100
# # print(1 in a)   # error dega

# b = "100"
# print("1" in b)


# create a list of fruit name and take input from user and check is available or not 

# fruit = ["mango", "guave", "papaya","peer" , "litchi"]
# n = input("enter your fruit :").lower() 
# # .lower() = it is used for converting in small letter
# print(n in fruit)



# sd=10, # we can apply membership operator
# as=10  # we cannot


# name = "mohan"
# print("y" not in name)
# print("m" in name)
# print("m" not in name)

# s= 10,20,30,40
# print (25 in s)
# print (20 in s)

# b = [20,30,50,60]
# num=input("enter your number :")

# print (num in b )


# range = it is a method used for convert the int iterator to eterable data type
# it is always for integer , and value is always less than 1 

n = 100
print(10 in range(n))
print('10' in range(n))
# print(10 in n)    error

v = True 
print("T" in str(v))
# print("T" in v) # error


#   Identity operator :- id() = memory location
                        #  is , not is = operator h identity compare krta h 
                        
#  -> it compare based on memory location.  
#  -> id() : this method is used to find the memory location of variable Value.
 
 
a=10
b=10
print (a==b)
 
mla=id(a)
mlb=id(b)  
print("memory location of a =",mla)
print("memory location of b =",mlb)
print(a is b) 

# # case 1 : if both variable name are different and value are same then
#               memory location be will be same

v = 10
a = 10 
print(id(v))  
print(id(a)) 
print(v is a)
print(v is not a)


# case 2 : if variable name is same and value are different then memory location will be different

v= 10
print (id(v))
v= 20
print (id(v))
print(v is v)
print(v is not v)


# case 3 : if variable name is diff and value are different then memory location will be different


v= 10
a= 20
print (id(v))
print(id(a))

print(v is a)
print(v is not a)

 #case 4:  if both variable name are same and value are same then memory location be will be same

v= 10

print (id(v))
v = 10
print(id(v))

print(v is v)
print( v is not v)


# #  #  logical operator 
 
# # #  1) and  # for both true 
 
# # a=10
# # b=30
# # print(a>0 and b<40)  # true
# # a=-10
# # b=30
# # print(a>0 and b<40)  # f
# # a=10
# # b=200
# # print(a>0 and b<40) # f
# # a=-10
# # b=200
# # print(a>0 and b<40) # f

# # print(True and True)
# # print(True and False)
# # print(False and True)
# # print(False and False)

# # print(1 and 1)
# # print(1 and 0)
# # print(0 and 1)
# # print(0 and 0)
 


# ui="md@123" 
# pwd="md123"

# userid=input("Enter your user id: ")
# userpwd=input("Enter your user pwd: ")

# # print(ui==userid and pwd==userpwd)

# if (ui==userid and pwd==userpwd) :
#     print("login successful")
#     print("start")
    
# else:
#     print("check your id and pwd")
 
 
 
 
 
# #  2) or   # dono me se ek true to true hoga

# a=10
# b=30
# print(a>0 or b<40)  # true
# a=-10
# b=30
# print(a>0 or b<40)  # t
# a=10
# b=200
# print(a>0 or b<40) # t
# a=-10
# b=200
# print(a>0 or b<40) # f

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(1 or 1)
# print(1 or 0)
# print(0 or 1)
# print(0 or 0)



# print(" who is the pm of india ?")
# print("a.mohan")
# print("b.modi")
# print("c.mohan")
# print("d.johan")

# ans=input("Enter your pm: ")
# if ans=="B" or ans=="b":
#     print("your answer is correct.")

# else:
#     print("you are wrong.")



# n=int(input("enter your no: "))
# a=n%3
# b=n%5
# if a==0 and b==0:
#     print( "number is divisible by both" )
    
# else : 
#     print("not divisible by both")



#  3) not
 
 
# a=10
# print(not a>0) # false
 
# print(not(True))
 
print(not (1)) 
