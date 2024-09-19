#-----------------------------------#
# Introduction to Loops in Python   #
#-----------------------------------#

# There are the following types of loops in python #

# => While Loop <= #

# i=1
# while i<=5:
#     print("Hello! I am Here...")
#     i+=1
# print("Loop Ended!")

# j=1
# while j<=100:
#     print(j)
#     j+=1
# print("Loop Ended!")

# k=100
# while k>=1:
#     print(k)
#     k-=1
# print("Loop Ended!")

# a,b=1,5
# while a<=10:
#     c=b*a
#     print("5*{}={}".format(a,c))
#     a+=1
# print("Loop Ended!")


# num=[1,4,9,16,25,36,49,64,81,100]
# index=0
# while index<len(num):
#     print(index,num[index])
#     index+=1

# treverse 
# num2=(1,4,9,16,25,36,49,64,81,100)
# x=0
# ToFind=81
# while x<len(num2):
#     if(num2[x]==ToFind):
#         print("element is found on index:",x)
#         break
#     else:
#         print("Searching...")
#     x+=1

# num=1
# print("list of odd numbers till 10:")
# while num<=10:
#     if(num%2==0):
#         num+=1
#         continue
#     print(num)
#     num+=1

# => For Loops <= #

# num= [1,3,4,7,8,3,6,0,31]
# for val in num:
#     print(val)

# str1="Hi! I am Here ...."
# for char in str1:
#     print(char)

# num2=[1,33,44,13,575,22,52,52,8]
# x,indx=52,0
# for ele in num2:
#     if(ele==x):
#         print("Elemnet is found at index:",indx)
#     indx+=1

# Range & Pass function in for loop #

# for num in range(10):
#     print(num)

# for num1 in range(1,20):
#     print(num1)

# for val in range(0,101,4):
#     print(val)

# for value in range(1,101):
#     pass
# print("loop is passed using pass else it will give error!!!")