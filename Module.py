# module:- collection of funcion is known as module
# every python file treat as a module(.py file)

# why we are creating module 
# for access one file data to another file data or one function data to another function data 
# we are using module concept with import 

#  how to create Module :- 


import mainmodule
# print(mainmodule.v)
# print(mainmodule.v1)   # ye error dega q  ki ye nhi h 

mainmodule.greet("j pan")

mainmodule.add()

print(mainmodule.fee(12000))

#  how to rename module during run-time

import mainmodule as md 
print(md.v)
md.add()

# how to acess particular data from another module  

from mainmodule import add, greet
add()
greet("md")

from mainmodule import*
add()
greet("md")

from mainmodule import add


