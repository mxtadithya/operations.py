file=open("examplehandiling.txt","w")
# file.write("Hello adithya!\n")
# file.write("good morning")
# # content = file.read()
# # print(content)
# file.close()

#using with

# #write..............
# with open("handiling.txt","w")as file:
#     file.write("halooo\n")
# #append.............
# with open("handiling.txt","a")as file:
#     file.write("halooo guys")
# #read..........    
# with open("handiling.txt","r")as file:
#         print(file.read())


# f = open('students.txt','w')
# for i in range(1,11):
#     f.write('Hello'+'\n')
    
# f = open('students.txt','r')

# data = f.read(3)
# print(f.tell())
# f.seek(0)
# print(f.tell())
# data1 = f.read()

# print(data)
# print(data1)

# first_line = f.readline(2)
# remaining = f.readline()
# print(first_line)
# print(remaining)

# data = f.readlines()
# for i in data:
#     print(i)

#module access cheyyunnath
# import functions
# from functions import is_even
# print(is_even(8),'file handling')
# print(functions.is_even(10))


import os

# os.remove('sample.txt')

# if os.path.exists('sample.txt'):
#     os.remove('sample.txt')
    
# os.rmdir('folders')

import math
# print(math.floor(8.12))
# print(math.sqrt(8.12))
# print(math.ceil(8.12))
# print(math.pi)
import random
from datetime import datetime,date
print(math.floor(random.random()*1e6))
print(random.randint(1,9))
print(random.choice(['blue','black','green']))
now = datetime.now()
print(now)
print(now.date())
print(now.month)
print(now.day)
print(now.year)
print(date.today())
