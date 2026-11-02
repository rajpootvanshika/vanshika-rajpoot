#FOR LOOP
# kaha se jana hai -> kaha tk jana hai-> kaise jana hai
# 1-50

# #while loop
# kaha se jana hai-> kab tak jana hai-> kaise jana hai

# while jab tak yeh condition true hai:
# tab tak yeh code chalega.
#1-50 tak print krna hai using while loop. 

# i=1
# while i<=10:
    # print(i)
    # i=i+1
#10-1 print krna hai using while loop.
# i=10
# while i>=1:
#     print(i)
#     i=i-1

#ques user se password mangte raho kn tk jab
#  tk password "abhishek123" na mil jaye.
password=""
# while password != "abhishek123":
#     password=input("enter the password:")
# print("access granted")

#ques- print table of any number which user
#  gives using while loop
# n=int(input("enter your number:"))
# i=1
# while i<=10:
#    print(n*i)
#    i=i+1

#print even numbers from 2 to 20
# i=2
# while i <=20:
#    print(i)
#    i=i+2
 #print sum of 2 to 20 even nums
 
#ques print a number in reverse order
# n=1234-> 4321
# n=1234
# a=0
# while n>0:
#     last=n%10
#     a=a*10+last
#     n=n//10
# print(a)

# #number kitne digit ka hai
# n=1234

#question is armstrong or not.
n=153
length=len(str(n))
sum=0
temp=n
while n>0:
    last=n%10
    sum=sum+last**length
    n=n//10
    if sum==temp:
        print(f"{temp} is armstrong number")
    else:
        print(f"{temp}is not armstrong number")

#

    



 