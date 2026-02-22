#  #  control statement :-  Decision making satement
 
# in which order you want to run the code 
# change the flow of code 
 
 
#  types of control statement
 
# 1) condition                 2)  transfer                                   3)  looping/iterative 
 
#  simple if                     it depend on condition                         a) for : when fix  time 
#  if else                       break : terminate the current  ,,              b) while : when not  fix time
#  elif if ladder                continue : skip the current execution path
#  nested if elif                pass :  block (use this :)
#                                      it is used for create the empty block
 
 
 
 # conditional statement
 
 # 1) simple if :-  it apply only on one condition
#  if  statement run the block of code when condition is True
 
 
a=int(input("Enter your number: "))

if a>0 :
    print("hii")
    print("hello")
    print("you are dump")
    print("this is the end")
print("you are very enthaustic teacher")
 
#  # how to create the block in python 
#  by using the (:) colon  we can create the block in  python
 
# how we can consider block of code
# after (:) colon all code should be in same line vertically  
 

num=int(input("Enter your number: "))
if num%2==0 :
    print("Even number")
    print("same")
print("this is not code:")
if num%2!=0:
    print("odd number")         
    print("this is not:")                      
                           
    # syntax error = voilet rule of python
    # indentation error = jab line vertically se hat jaye 
 

# program for even odd function:-

# num=int(input("Enter your numer: "))
# if num%2==0:
#     print("EVEN NUMBER")
#     print("true")
# else:
#     print("ODD NUMBER")
        

# # write a program to check given no is divisible by three or not

# if num%3==0:
#     print("divisible by 3")
# else:
#     print("not divisible")
    
    
# # write a program to check name in list 

# m=["mohan","sohan","aman","manata bhabhi"]
# name=input("Enter your friend name: ")

# if name in m:
#     print("your friend name is exit")
    
# else:
#     print("your friend is not in this list")
    
    
    # write the program to check the given no is 5 or 7 both are divisible
    
# n=int(input("Enter your number:"))
# if n%5==0 and n%7==0:
#     print("is divisible")
# else:
#     print("not")

# # title()= it is used for  
# list=["aalu","kobi","mango","daal chawal"]
# name=input("Enter your food name: ").lower()
# if name in list:
#     print("available")
# else:
#     print("Sorry not available")
    
# #  write a program to check a leap year  
# year=int(input("Enter the no of day in your year:"))

# if year%4==0:
#     print("leap year")
# else:
#     print("not leap year")
    
    
    
#  write a program to check given no is +ve or -ve. 

# n=int(input("Enter your number: "))
# if n>=0 :
#     print("positive")
# else:
#     print("negative")
    
    
# wap to check you are eligible for vote or not 

# n=int(input("Enter your number: "))
# if n>=18:
#     print("you are eligible")
# else:
#     print("you are not")
    
    
# wap to check the given no is divisible by 3 or 5

# n=int(input("Enter your number:"))
# if n%3==0 or n%5==0:
#     print("is divisible by 3 or 5")
# else:
#     print("not diviible")
    
    
# write a program to check the given last digit no is even or odd

# n=int(input("Enter your number:"))
# last_no=n%10
# if last_no%2==0:
#     print("enen")
    
# else:
#     print("odd")


# wap to check your name first letter is vowel or not

# vowelname=["a","e","i","o","u"]
# name=input("Enter your name: ").lower()
# first_letter=name[0]
# if first_letter in vowelname :
#     print("your name first letter is vowel")
# else :
#     print("consonant")

# WAP for age is greater than 20 and job status is yes

# n=int(input("Enter your age: "))
# job=input("Enter your job status in yes or not ")

# if n>=20 and job=="yes":
#     print("you are eligible")
    
# else :
#     print("not eligible")


# WAP to check your mobile no first digit is even or odd

a,b,c,d,e,f,g,h,i,j,=map(int,input("Enter your number: ").split())
# print(a)
rem=a%2

if rem==0 : 
    print("even number")
else:
    print("odd number")
    

# elif ladder :- 
# this statement is used for multiple condition.
# condition should be more than two 

# syntax :
    
# if condition:
#         # block of code 
# elif condition:
#         #block of code
# elif condition:
#     #
# elif condition:
# .
# .
# .
# else:
#     # block of code    

# WAP to check the given number is +ve , -ve or zero
# n=int(input("enter your number: "))

# if n>0:
#     print("+ve")
# elif n==0:
#     print("zero")
# else:
#     print("-ve")
    



#  WAP to check the grade base don marks :

# marks=int(input("Enter your marks: "))

# if marks<0 or marks>100:
#     print("your marks is invalid.",marks)
# elif marks>90 and marks<=100:
#     print("grade= A++")
# elif marks>80 and marks<=90:
#     print("grade = A",marks)
# elif marks>70 and marks<=80:
#     print("grade = B",marks)
# elif marks>60 and marks<=70:
#     print("grade = C",marks)
# elif marks>50 and marks<=60:
#     print("grade = D",marks)
# else:
#     print("Fail",marks)



# WAP to show 

# data=input("Enter Anything : ")
# if data>="a" and data<="z":
#     print("lowercase")
# elif data>="A" and data<="Z":
#     print("UPPERCASE")
# elif data>="0" and data<="99":
#     print("digit")
# else:
#     print("special symbol")
    
    
# WAP to check the greatest among 3 number 

# method 1:

# n1=int(input("enter your n1:"))
# n2=int(input("enter your n2:"))
# n3=int(input("enter your n3:"))
# if n1>n2 and n1>n3:
#     print(n1,"is greater")
# # elif n2>n3 and n3>n1:
# elif n2>n3:
#     print(n2,"is greatest")
# else:
#     print(n3,"is greatest")
    
  # method 2 
   
# a,b,c=map(int,input("Enter your number").split())

# if a>b and a>c:
#     print(a,"is greater")
# elif b>c and c>a:
#     print(b,"is greatest")
# else:
#     print(c,"is greatest")   



# if age is greater than 21 and salary is greater than 50k print msg will get he will marry very soon
# if age is greter than 21 and salry is 30-50k marry 1st year
# if age is greter than 21 and salry is 10-30k msg = first increase your salary then marry
# if age is greater than 21 and salry less than 10k msg dont think about marriage

# age=int(input("Enter your age :"))
# salary=int(input("Enter your salary: "))

# if age>21 and salary>=50000:
#     print("marry very soon")
# elif age>21 and salary>=30000 and salary>50000:
#     print("marry after 1 year")
# elif age>21 and salary>10000 and salary>30000:
#     print("increase your salary then marry")
# else:
#     print("dont think about marriage")



# Nested if else :




# user_id="md@123"
# pwd="123"
# euser_id=input("Enter user id: ")

# if euser_id==user_id :
#     epwd=input("Enter the password : ")
#     if epwd==pwd:
#         print("Login successful")
#     else:
#         print("check your password")
# else:
#     print("check your user id")



# check positive or negative if positive then check even or odd

# num=int(input("Enter the number: "))
# if num>0:
#     if num%2==0:
#         print("even number")
#     else:
#         print("odd")
    
# else:
#     print("negative")


# n=int(input("Enter your number: "))

# if n%3==0:
#     if n%5==0:
#         print("divided by both ")
#     else:
#         print("only divisible by 3")
# else:
#     print("not divisible by 3")
    
    

# three number are short the three numner in ascending or descending order

a,b,c=map(int,input("Enter the three num: ").split())

if a>b and b>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>c :
    if a>c:
        print(b,a,c) 
    else:
        print(b,c,a)  
else:
    if a>b:
        print(c,a,b)
    else:
        print(c,b,a)
    

# v1=input("Enter your class 10th status pass or fail").lower()
# if v1=="pass":
#     v2=input("Enter your 12th status pass or fail").lower()
#     if v2=="pass":
#         stream=input("Enter your scream science(pcm), commerce,art").lower()
#         if stream=="science" or "pcm":
#             print("you can get admission in engg clg")
#         elif stream=="commerce":
#             print("you are at commerce stream")
#         else:
#             print("you are a arts student")
#     else:
#         print("first pass in 12th")
# else:
#     print("first of all pass the 10th")

# fee attende mid

# fee=input("enter your fee status paid or not: ").lower()
# if fee=="paid":
#     attendence=int(input("Enter your attendence in percenage:"))
#     if attendence>=75:
#         midsemresult=input("Enter your midsem pass or fail: ").lower()
#         if midsemresult=="pass":
#             print("your form will be forwarded ")
#             print("CONGRATULATIONS")
#         else:
#             print("first pass in midsem")
        
#     else:
#         print("your attendence is less")
# else:
#     print("paid your amount first")
