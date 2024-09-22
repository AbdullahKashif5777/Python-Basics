#--------------------------#
# File Handling in Python
#--------------------------#

# Create a  file #
# f=open("info.txt","w")
# f.close()

# # Write data in file #
# f=open("info.txt","w")
# f.write("Hello! Congrats your file is created ...")
# f.close()

# Read data from file #
# f=open("info.txt","r")
# text=f.read()
# print(text)
# f.close()

# Add data at end of file without changing previous data#
# f=open("info.txt","a")
# f.write("\n now u can store data here....")
# f.close()

# write data and without keeping previous data #
# f=open("info.txt","w")
# f.write("Name:Ali\nAge:20\nNationality:Pakistani")
# f.close()

# read & add data in file #
# f=open("info.txt","a+")
# f.write("\n now u can store data here....")
# f.seek(0) # as pointer is att end of file so move it at starting #
# text2=f.read()
# print(text2)
# f.close()

# Read by line By line #
# f=open("info.txt","r")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# f.close()

# => Using with Syntax <= #
# with open("practice.txt","w") as f:
#     f.write("New file ! practice.txt is created..")

# add something to file #
# with open("practice.txt","a+") as f:
#     f.write("\nNew data added.....")
#     f.seek(0)
#     text4=f.read()
#     print(text4)

# check file exists or not #
# import os
# if os.path.exists("practice.txt"):
#     print("file exists !.....")
# else:
#     print("file not found !...")

# Remove a file #
# import os
# os.remove("practice.txt")