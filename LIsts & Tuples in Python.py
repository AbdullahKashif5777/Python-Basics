#----------------------------------#
# Introduction to Lists in Python
#----------------------------------#

# => General Introduction #

# numbers=[1.2,2.1,3.3,5.5]
# print(numbers)
# print(numbers[3])
# print(type(numbers))
# print(len(numbers))

# => Also list can store different types of data #

# data=["Ali",1,3.1,'a',"Boy"]
# print(data)
# print(data[0],",",data[2])
# print(type(data))
# print(len(data))

#----------------------------------#
# Slicing of  Lists in Python
#----------------------------------#

# marks=[99,20,73,64,88]
# print(marks[1:],",",marks[:len(marks)])
# print(marks[1:4])
# print(marks[len(marks):-1])
# print(marks[-3:-1])

#------------------------------------------#
# Some Basic Functions of Lists in Python
#------------------------------------------#

# list=[1,0,9,2,8,3,7,4,6,5]
# list.append(1) # To anything at end of list #
# print(list)

#=> if we do 

# print(list.append(2)) # it does not give any list as append function dont have any return type so it return None #
 
 # => In order to add anything in last ina list we can do

# list+=[1] # By concatination

# => In order to add we can use Walrus Operator (:=) to add something new in list and to return at same time #

# print(NewList:=[1,0,2,9,8,3,7,4,6,5]+[1])

# lists=[1,0,2,9,3,8,4,7,6,5]
# lists.sort() # sort the list in asending order #
# print(lists)
# lists.sort(reverse=True) # sort the list in desending order #
# print(lists)
# lists.reverse() # reverse the string from backword to forward #
# print(lists)
# lists.insert(5,'a') # insert object at certain index #
# print(lists)
# lists.remove(1) # remove the element at its first occurance #
# print(list)
# lists.pop(5) # remove the element at that index #
# print(lists)

#----------------------------------#
# Introduction to Tuples in Python
#----------------------------------#

# Tuples are unchangeable after declaration 

# tup=(1,2,3)
# print(tup)
# print(type(tup))

# tup1=(1,) # it is neccesery to use (,) after single element otherwise it will be consider as integer
# tup2=(1)
# print(type(tup1),",",type(tup2))

#----------------------------------#
# Sclicing of Tuples in Python
#----------------------------------#

# marks=(99,'a',73,64,88)
# print(marks[1:],",",marks[:len(marks)])
# print(marks[1:4])
# print(marks[len(marks):-1])
# print(marks[-3:-1])

#-----------------------------------#
# Basic Methods of Tuples in Python
#-----------------------------------#

# tup3=(1,2,3,4,5,6,6,2,1)
# print(tup3.index(2)) # return the index of that element where it ocures first time #
# print(tup3.count(1)) # count the no of occurance of that element #







