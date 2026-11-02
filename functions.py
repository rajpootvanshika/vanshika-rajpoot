# a=121
# rev=0
# copy=a
# while a!=0:
#     rev=rev*10+a%10
#     a=a//10

# if copy==rev:
#     print("pallindrome")
# else:
#     print("not a pallindrome")

#user defined fuctions
#defining a fuction
def hello():
    print("how are you")

#calling a function
#hello()

#RETURN
# def hey():
#     return"how are you"#return the value to the calling block
# a=hey()#calling block captures the value
# print(a)

#parameters and arguments
# def addition(a,b):#you accept the parameters
#     print(a+b)
# addition (10,20)#and you provide the #arguments to te parameters
# addition(50,50)

# def pallindrome (a):
#     a=121
#     rev=0
#     copy=a
#     while a!=0:
#         rev=rev*10+a%10
#         a=a//10
#     if copy==rev:
#         print(copy)
# for i in range(1,1000):
#     pallindrome(i)
    
#parameters and arguments
#default parameters
# def hello(a,b,c,d,e=30):
#     print(a+b)

# hello(50,50,20,56)

#print numbers from 1-30
#you cannot use while and for loop
#YOU CANNOT USE PRINT STATEMENT MORE THAN 1

# def numbers(n):
#     if n==100:
#         return
#     print(n)
#     numbers(n+1)

# numbers(1)

# def numbers(n):
#     if n==31:
#         return
#     numbers(n+1)
#     print(n)

# numbers(1)

#data structures
#1. square brackets -> list[]
#2. heterogenous data structure(a list can store diff type of data type)
#list allow storing duplicate values.
#list are ordered bcz they have indexing and indexing starts from 0
#marks =[] #empty list
# marks=[80,78,90,65,88,87,75,"abhishek",3.14]
# marks[3]="modiji"
# marks(marks[3])

#traversing
a=[10,20,30,40,50]
for i in a:
    print(i)