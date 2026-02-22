# looping statement:- repeating the block of code is called l.p statement 

# for loop:-

# syntax rule :
    
#     for loopvariable mem.operator EDT :             EDT- list , tuple, set, dictionary, string
#         block of code 
        
        
        
        
# name="mdfirdous"
# for v in name:
#     print(v)
    
# name="mdfirdous"  
# for i in name:
#     print("v")
    

# for i in "100":
#     print("md firdous  class cse")
  
# for i in range(100)  :
#     print("md firdous")   


# for i in range(15):
#     print(i)

# user ke hisab se name or how many time 

# name=input("Enter your name: ")
# times=int(input("Enter your how many times: "))

# for i in range(times):
#     print(name)


# for i in range(10):
#     print("md firdous", end=" ")

# end=" " =  vertical se horizontal ek line me lata h 
# ek hi line me lane ke liye


# print the even number from 0 to 100

# i=i%2==0

for i in range(0,101,2):
    print(i,end=",")
    
for i in range(101):
    if i%2==0:
        print(i,end=",")

# name="mohan"
# for i in name:
#     print(i, end=" ")
    
# # WAP to count the number of character present in name

# name=input("Enter your nice name: ")
# c=0
# for i in name:
#     c=c+1
#     print(c)
# print("no of character=",c)
    

# WAP which show vowel in your name
# method 1

# name=input("Enter your nice name: ").lower()
# for v in name:
    
#     if v in ["a","e","i","o","u"]:
#         print(v)

# # method 2

# name=input("Enter your nice name: ").lower()
# for v in name:
#     if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
#         print(v)


# WAP which show no. of vowel in your name

# name=input("Enter your nice name: ").lower()
# c=0
# for v in name:
    
#     if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
#         c=c+1
#         print(v)
# print("no of vowels=",c)

 
 # WAP to count the no of character , no of vowels , no of consonant
# name=input("Enter your nice name: ").lower()
# nv=0
# nc=0
# no_of_c=0
# for md in name  :
#     nc=nc+1
#     if md=="a"or md=="e"or md=="i"or md=="o" or md=="u":
#         nv=nv+1
#         # print(md)
#     else:
#         no_of_c=no_of_c+1
# print("no of vowels",nv)
# print("no of character=",nc)
# print("no of consonant=",no_of_c)       



# name=input("Enter your nice name: ").lower()
# for v in name:
#     if v in "aeiou":
#         print(v)




# RANGE
 
# num=int(input("Enter your number: "))
# for i in range(num)
# for i in range(0,num)

# num=int(input("Enter your number: "))
# for i in range(0,num+1,2):
#     print(i)
    
    
# num=int(input("Enter your number: "))
# for i in range(10,num-1,-1):
#     print(i)
    
    
    
# syntax of range;
   
# range(start_value,end_value, step_value)
# lower to higher -> step value = +ve
#higher to lower -> step value = -ve
# range default value start from zero
# range end will be always less than 1 from given number
# default step value will be 1


# n=10
# for i in range(n):
#     print(i,end=" ")
#     print("mohan")
#     print("sohan")
#     print("*")
#     print(''' 
#           ******
#           *    *
#           *    * 
#           *    *
#           ******
#           ''')
# print("no of character=",i)  # ye loop ke bahr h isliye ye sirf last value ko store kr rha h (n-1)

# WAP to check given 
# n=int(input("Enter number: "))
# for v in range(1,n+1):
#     if v%3==0 and v%5==0:
#         print(v)
        
# m=["aman","janu","babu","sona","jadu","mohan"]  

# name=input("Enter your name: ").lower()
# for i in m:
#     if i==name:
#         print("you are my best friend")
#         break
#     else:
#         print("dusmaan")
#         break
      


# WAP to check item is available if available then order confirmed otherwise sorry not available

# food=["chawal","daal","chiwra","maggi","pasta","masala"]
# f=input("Enter your food item name: ").lower()
# for v in food:
#     if v==f:
#         print("your ordered is confirmed")
#         print("order successful")
#         break
# else:
#     print("item is not available")
        

# n=100
# for i in range(n+1):
#     print(i)  
#     # if i==50:
#     if i>10:
#         break
         
        
 
# name="mdfirdous"
# lg=len(name)
# for i in range(lg):
#     # print(i) 
#     print(name[i])
#     if i==2:
#         break
 
 # WAP a program to for factor
 
n=int(input("Enter the number: "))
c=0
f=1
for i in range(1,n+1):
    f=f*i
    if n%i==0:
        print(i,end=" ")
        c=c+1
print("count=",c)
print("factorial=",f)
    
 
 
# WAp to check the given number is  prime number or not

# n=int(input("Enter the number: "))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#         c=c+1
# print("no of count",c)

# if c==1 or c>2:
#     print("not prime number ",n)
# else:
#     print("prime number",n)
  
# if c==2:
#     print("prime number",n)
# else:  
#     print("not prime number ",n) 

# method 2

# n=int(input("Enter number: "))
# if n<=1:
#     print("not a prime number")
# else: 
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number") 


# n=int(input("Enter number: "))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")
    

# WAP to swap two number

# a=10
# b=20
# print("before swap",a,b)

# t=a
# a=b
# b=t
# print("after swap",a,b)   


# fibonacci

# a=-1
# b=1
# n=int(input("Enter number")) 
# for i in range(n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
      
      
# WAP to check the given number or string is a palindrome or not
# print the all prime number from 1 to 100
      




 # nested for loop

# for amit in range(6):
#     for aman in range(6):
#         print(amit,end=" ") 
#     print()
    
  
  
# for amit in range(6):
#     for aman in range(6):
#         print(aman,end=" ") 
#     print()

# make star in square:-
# n=int(input("Enter your number: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
    

# n=int(input("Enter your number: "))
# for i in range(n):
#     for j in range(n):
#         print("md & firdous",end=" ")
#     print()
    
    
# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()
    
    
# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")


# print(ord("A"))
# print(ord("a")) # ASCII value
# print(chr(97)) 


# s="abcdefghijklmnopqrstuvwxyz"
# # for i in s:
# #     print(ord(i))

# # print(ord(i))

# for j in s.upper():
#     print(ord(j),end=" ")

# n=int(input("Enter your number: "))
# for i in range(65,n+1):
#     print(i,":",chr(i))


# for i in range(6):
#     for j in range(6):
#         print(chr(65+i),end=" ")
#     print()
    
# n=int(input("Enter your number: "))
# for i in range(65,65+n):
#     for j in range(4):
#         print(chr(i),end=" ")
#     print()


# n=int(input("Enter the number of row "))
# for amit in range(6):
#     for aman in range(amit+1):
#         print("*",end=" ")
#     # print()



#  inverted triangle    
# for amit in range(6,0,-1):
#     for aman in range(amit-1):
#         print("*",end=" ")
#     print()


# n=int(input("Enter your number: "))
# for i in range(1,n+1):
#     # print(i)
#     if i%2==0:
#         print(i,end=" ")
#     # print("even number")

    # if i%2!=0:
    #     print(i,end=" ")
    # # print("Odd number")
    
    
# name=input("Enter your name: ")
# c=0
# vc=0
# for i in name:
#     c=c+1
#     if i in "aeiou":
#         vc=vc+1
#         print(i,end=" ")
#     print("*")
# print(c)
# print("vowels=",vc)    
    
      
# sum of natural number

# n=int(input("Enter your num:"))
# s=0
# for i in range(1,n+1):
#     s=s+i
# print(s)

# sum of even number
# method1

# n=int(input("Enter your num:"))
# s=0
# for i in range(1,n+1,2):
#     s=s+i
# print(s)

# method2

# n=int(input("Enter your num:"))
# es=0
# ec=0
# s=0
# odd_sum=0
# for i in range(1,n+1):
#     s=s+i
#     if i%2==0:
#         es=es+i
#         ec=ec+1  
#     else:
#         odd_sum=odd_sum+i 
        
        
# print("sum of even number",es)
# print("count of even number",ec)
# print("sum of natural number",s)
# print("sum of odd number",odd_sum)



# c=0
# ds=0
# for i in range(50,502):
#     if i%3==0 and i%5==0:
#         print(i,end=" ")
#         c=c+1
#         ds=ds+1
# print("sum of all divisible no=",ds)
# print("no of count=",c)

n=10
p=1
s=0
for i in range(1,n+1):
    p=p*i
    s=s+i
print("sum of natural no=",s)
print("product of natural no=",p)



n=int(input("Enter number: "))
if n<=1:
    print("not a prime number")
for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("prime number")



   # while loop:-
#  -> while loop is known as entry control loop , means first condition will check
#  -> if you don't know how many times block of code will be executed then we will use while loop

# syntax:-

# while condition:
#     block of code
   
# example1   
# n=10 
# i=0
# while i<n:
#     print("mohan")
#     i=i+1 # it is used always for ending the loop 
 

# example2
# name="mohan" 
# lg=len(name) 
# i=0
# while i<lg:
#     print(name[i])
#     i=i+1
 
 
 # WAP to print all even number from 1 to 100   
# for i in range(1,100):
#     if i%2==0:
#         print(i,end=" ")

# i=1
# while i<=100:
#     if i%2==0:
#         print(i,end=" ")
#     i=i+1
 

# wap 50 se 500 odd number uska sum 
# wap to print the sum of all number from 50 to 500 by using for and while loop
# s=0
# c=0
# for i in range(50,501) :
#     if i%2!=0:
#         print(i, end=" ")
#         s=s+i
# print("sum of odd number=",s)
    


# i=50
# s=0
# c=0
# p=1
# while i<=500:
#     if i%2!=0:
#         s=s+i
#         c=c+1
#         p=p*i
#     i+=1
# print("sum of odd number=",s)
# print("count of odd no=",c)
# print("product of all odd number=",p)


# character count, vowel count , kaun kaun vowel
# name=input("Enter your nice name:")
# c=0
# vowel=0
# for i in name:
#     if i in ["a","e","i","o","u"]:
#         print(i,end=" ")
#         vowel=vowel+1
#         # print(name[i])
#     c=c+1
# print("no of character=",c)
# print("no of vowel=",vowel)



# while True:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     s=a+b
#     print("sum of two number",s)
   #  ans=input("if you want to add again press Enter:")
   #  if ans=="":
   #      continue
   #  else:
   #      break
           
        
user_id=[]
user_pwd=[]

while True:
    eui=input("Create the user Id: ")
    epwd=input("Create the password: ")
    user_id.append(eui)
    user_pwd.append(epwd)
    ans=input("for creating new user id and pswd press 1 otherwise Exit: ")
    if ans=="1":
        continue
    else:
        print("loop is finish")
        break
print(user_id)
print(user_pwd)
for ui in user_id:
    Enter_ui=input("Enter your user id: ")
    if ui in Enter_ui:
        for pd in user_pwd:
            Enter_pwd=input("Enter the user password: ")
            if pd in Enter_pwd:
                print("login is successful")
                break
            else:
                print("not login ")
                print("check password")
                break
        else:
            break
        
    else:
        print("check your userid ")
        break
print(user_id)   
print(user_pwd)  
enter_u=input("Enter your user id ")
if enter_u in user_id:
    Enter_pwd=input("Enter your password")
    if Enter_pwd in user_pwd:
        print("successful")
    else:
        print("check your password")
else:
    print("check your user id")
        
 

    

