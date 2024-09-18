#--------------------------------#
# Intro to Dictionary in Python
#--------------------------------#

# info= {
#     "Names": ["Ali","Ahmad","Haseeb","Hammad"],
#     "Ages":[15,16,17,18],
#     "Cgpa":[3.3,3.4,3.5,3.6],
#     "Semester":(1,1,1,1),
#     "person":"Ali",
#     "marks":30.5,
#     1:2,
#     2:"Name",
# }
# print(info)
# print(info["Names"])
# print(info["Ages"])
# print(info["Cgpa"])
# print(info["Semester"])
# print(info["person"])
# print(info["marks"])
# print(info[1])
# print(info[2])

#--------------------------------#
# Nested Dictionary in Python
#--------------------------------#

# dic={
#     "Name":"Ali",
#     "Program":"Software Engineering",
#     "Programing Languages":{
#         "C++":"Basic",
#         "Java":"Advance",
#         "Python":"Expert",
#     }
# }
# print(dic)
# print(dic["Programing Languages"])
# print(dic["Programing Languages"]["Python"])

#-----------------------------------------#
# Basic Functions of Dictionary in Python
#-----------------------------------------#

# dic_Key={
#     "Name":"Ali",
#     "Age":23,
#     "Marks":{
#         "Bio":88,
#         "English":79,
#         "Maths":98,
#     }
# }

# print(dic_Key.keys()) # Display all the keys of outer dictionary #
# print(tuple(dic_Key.keys())) # By typecasting into Tuple #

# print(dic_Key.values()) # show all the values in dictionary #
# print(dic_Key.items()) # return all the keys and values as tuples #
# print(dic_Key.get("Name")) # returns the values of key #
# print(dic_Key.get("name")) #if key doesnot exist in dictionary it returns none instead of error #
# dic_Key.update({"Cgpa":3.7}) # Update the dictionary by adding new key and its value #
# dic_Key.update({"Name":"Ahmad"}) # if the key already exist its override its value and update its value #
# print(dic_Key)

#--------------------------------#
# Intro to Sets in Python
#--------------------------------#

# info={1,2,"hello",'a',3.3,False} # sets are changeable but its elements are immutable #
# print(type(info))
# print(len(info))
# print(info)

# info1={1,1,3,2,2,6,"hello","hello",3} # here are duplicate values in set #
# print(len(info1)) # set count them in length but not display them twice #
# print(info1)  # Also set is unordered it will print values in random order at each run #

# emptyset=set() # its a right sayntax to create an empty set #

#-----------------------------------------#
# Basic Functions of Sets in Python
#-----------------------------------------#

# group=set()
# print(type(group))
# print(group)
# group.add("ali")
# group.add("Hello!")
# group.add((1,2,3))
# group.add(2) # add only single element in a set #
# print(group)
# group.remove(2) # remeoves only a single element from a set if it exists in set #
# print(group)
# print(group.pop())# display a random value from set #
# group.clear() # Makes set empty #
# print(group)

# set1={1,2,3,7,7,8,9}
# set2={1,2,3,4,5,6}
# print(set1.union(set2)) # combines  all the values of both sets and display a new set #
# print(set1.intersection(set2)) # prints all common elements of both sets #