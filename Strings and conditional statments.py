#------------------------------------#
# String Basic declarations
#------------------------------------#

# str1='hello'
# str2="hello"
# str3="""hello"""
# print(str1,"\n",str2,"\n",str3)

#------------------------------------#
# String Basic Functions
#------------------------------------#

# => Concatination

# str1="Hello"
# str2="World"
# print(str1+str2)

# => Length of string

# str1="Hello"
# str2="World"
# print(len(str1))
# print(len(str2))
# print(len(str1+" "+str2))

# => Indexing  & Slicing in String

# Indexing #

# str1="Hello World"
# print(str1[0],str1[3])

# Positive & Negative Slicing #

# print(str1[0:4])
# print(str1[:7])
# print(str1[6:])
# print(str1[:])
# print(str1[:-1])
# print(str1[-4:])
# print(str1[-12:])
# print(str1[:-12])
# print(str1[-9:-1])

# => Some demo functions

# str1="i am student & i am learning Python."
# print(str1.endswith(".")) # this functions checks the string ends with which character #
# print(str1.capitalize()) # Only captilizes first char of string #
# print(str1.replace("i","I")) # replaces the old char or group of char with new ones #
# print(str1.find("i")) # shows the index of char in string where it first times occures #
# print(str1.count("i")) # counts the occurance of substring #

#------------------------------------#
# Conditional Statments in Python
#------------------------------------#

# score=91
# if(score>=90):
#     print("A Grade")
# elif(score<90 and score>=80):
#     print("B Grade")
# elif(score<80 and score>=70):
#     print("c Grade")
# elif(score<70 and score>=50):
#     print("D Grade")
# else:
#     print("F garde")

# Example to check number is multiple of 5

# num=int(input(("Enter a number to check:")))
# if(num%5==0):
#     print("Number is multiple of 5")
# else:
#     print("Number is not multiple of 5")






