#-------------------------------------------#
#First Program to check how to print output #
#-------------------------------------------#

print("Hello World!")
print("Hello\nWorld!")
print("Hello","World!")
print("Hello""World!")

#-------------------------------------------#
# Input in Python # 
#-------------------------------------------#

age=input(("Enter your age:") )
print(type(age))
print(age)

agee=int(input(("Enter your age:")))
print(type(agee))
print(agee)

#-------------------------------------------#
# Operations in Python # 
#-------------------------------------------#

# => Arithmatic Operations 

a1=2
b1=5
print(a+b)
print(a-b)
print(a*b)
print(a/b) #( Always return answer in float)
print(a%b) #( Always return remainder)
print(a**b)#( Always used for  power of a number)

# => Assignment Operations 

a2=2
b2=2
a2+=b2
a2-=b2
a2*=b2
a2/=b2
a2%=b2
a2**=b2
print(a,"\n",b)

# => Relational / Comperision Operations

a3=2
b3=3
print(a3==b3)
print(a3!=b3)
print(a3<=b3)
print(a3>=b3)
print(a3<b3)
print(a3>b3)

# => Logical Operations

a4=2
b4=6
print(not(a4==b4))
print(not(a4!=b4))
print(not(a4!=b4) or (a4!=b4))
print(not(a4!=b4) and (a4!=b4))
print(a4 or b4)
print(a4 and b4)

#-------------------------------------------#
# Converstions in Python # 
#-------------------------------------------#

# # => Type conversion (Automatically by compiler)
a5=2
b5=4.5
sum=a5+b5
print(type(sum))
print(sum)

# # => Type casting (Manually by programer)

a6="4"
b6=2.2
c=int(a6)
print(b6+c)



