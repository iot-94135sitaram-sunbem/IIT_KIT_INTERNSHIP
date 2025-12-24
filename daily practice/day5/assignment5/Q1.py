import math as m

print(m.sqrt(16))


print(m.degrees(1))


print(m.radians(180))

import math as m

print(m.sqrt(16))


print(m.degrees(1))


print(m.radians(180))


print(m.cos(180))
print(m.sin(0))


print(m.log10(10))

print(m.factorial(5))

import os
print("current working directory = ",os.getcwd())


dir="sunbeam(created using os module)"
par_dir="D:\Temp"
path=os.path.join(par_dir,dir)
os.mkdir(path)

print(os.cpu_count())

print(os.getlogin())

print(os.getppid())

os.rename("os module.txt", "sitaram.txt")

file = open("sitaram.txt", "w")
file.write("Hello Python\n")
file.write("File handling using os module")
file.close()

file=open("sitaram.txt","r")
print(file.read())

