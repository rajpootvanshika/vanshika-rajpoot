# 12
"""name="nitish"
print(name)
age=18
print(age)   """

# name=input("enter your name : ")
# print(name) 

# data types 
# 1. numbers ->> int, float , complex 
# 2. string -->>
# 3.boolean -->> True or False 

# age=18
# score=34
# cgpa=7.8 or p/q 20/5

# age=20   #int 

# age=10j  #complex
# print(age) 


# string --> anything written inside "" is known as string 
# name = "fdsqghfr156789@#$%^_1234"  
# print(name)
# print(type(name))

# indexing and slicing 
# name="python"
# # # index -- >> 0,1,2,3,4,5 ,-1,-2,-3
# print(name[-1])

# slicing name[start index :stop index+1  : step value]
# name="sheryians"
# print(name[0:6:3])
# print(name[::-1])

# boolean -->> True or False 
# Falsy values -- >> 0,0.0,() ,  [] , {} ,"" ,None ,False 
# print(bool(0))
# print(bool(0.0))
# print(bool(()))
# print(bool([]))
# print(bool(""))
# print(bool(None))
# print(bool(False))
# print(bool("a"))

# arithmetic operators + , - ,/ ,* ,//,% - remainder , **
# a=10
# b=3
# print(10//2)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a%b)


# assignment operators 
# +=,-=,*=,/= ,//=,%=,**/
# a=10
# a**=3
# print(a)



# comparasion operators 
# <,><=,>= 
# ==  -- lhs = rhs,
# != -not equal 
# a=10
# print(a!=100)


# logical operators
# and , or , not 
# and if every condiiton is true then only it will give true as an output 
# otherwise it will give false if any one of the condition is false 
# print(10 > 8 and 20>15 and 20>8 and 35 > 36)

# print(10 > 8 or 20>15 or 20>8 or 35 > 36)

# print(not(10<8)) 

# input -- >> in input it take as an string
# name=int(input("enter your name : "))
# print(type(name))


# num=int(input("enter your number : "))
# if num>10:
#     print("greaterv than 10 ")
# elif num==0:
#     print("zero")
# elif num<10 and num>0:
#     print("num btwn 0 to 10 ")
# else:
#     print("num is -ve")

# check whe
# nested if else check if the num is +ve or -ve if +ve then check even or odd
# num=int(input("enter your num - "))
# if num>0:
#     print("+ve")
#     if num%2!=0:
#         print("odd")
#     elif num%2==0:
#         print("even")
# else:
#     if num%2==0:
#         print("-ve and even")
#     else:
#         print("+ve and odd")




# a=int(input("num1"))
# b=int(input("num2"))
# print(a+b)

# for loop 
# 10,9,8,,7,6,5
# sum=0
# num = int(input("enter your num  : "))
# for i in range(num,(num*10)+1,num):
#     print(i)

    

# n=5 --> 1,2,3,4,5
# sum=3
# sum=1+2
# sum=0
# n=int(input("enter your  number :"))
# for i in range(1,n+1,1):
#     sum+=i
# print(sum)
# name="naina"
# print(f"name: {name}")
# oddc=0
# evenc=0
# n=int(input("enter your range : "))
# for i in range(1,n+1): # 1,2,3,4,5,6,7,8,9,10
#     if i%2==0:
#         evenc+=1
#     else:
#         oddc+=1
# print(f"oddcount: {oddc} and evencount: {evenc}")