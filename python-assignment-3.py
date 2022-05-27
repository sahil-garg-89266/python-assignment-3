# QUESTION NO.1

print("Enter Your input as decimal number and get output as binary number")
x1=int(input())
x2=bin(x1)
print(x2)

print("")
# QUESTION NO.2

print("This is an interactive Python calculator program.")
x = input("Enter the expression only by using these operations (+,-,*,/,**,//,%) -:")
print("your answer is equal to-:",end=" ")
print(eval(x))

print("")
# QUESTION NO.3

import math as M

# (a) part

a1=3
a2=4
a3=5
print("Answer of part(a)-:",end=" ")
print((a1+a2)*a3)

# (b) part

print("Enter the value of n")
n=int(input())
print("Answer of part(b)-:",end=" ")
print(n*(n-1)/2)

# (c) part

print("Enter the value of r1")
r1=int(input())
print("Answer of part(c)-:",end=" ")
print(4*(M.pi)*(r1**2))

# (d) part
r = int(input("Enter the value of r-: "))
a = int(input("Enter the value of angle a-: "))
b = int(input("Enter the value of angle b-: "))
print("Answer of part(d)-: ",end=" ")
print(((r*((M.cos(a))**2)) + (r*((M.sin(b))**2)))**(0.5))

# (e) part

x1 = int(input("Enter the value of x1-: "))
x2 = int(input("Enter the value of x2-: "))
y1 = int(input("Enter the value of y1-: "))
y2 = int(input("Enter the value of y2-: "))
print("Answer of part(d)-: ",end=" ")
if x2 == x1:
    print("NOT DEFINED")
else:
    print("y2-y1/x2-x1 = ", (y2 - y1)/(x2 - x1))

print("")
# QUESTION NO.4

print("In the range(5)")
for i in range(5):
    print(i)

print("In the range(3, 10)")
for i in range(3, 10):
    print(i)

print("In the range(4 ,13, 3)")
for i in range(4 ,13, 3):
    print(i)

print("In the range(15, 5, -2)")
for i in range(15, 5, -2):
    print(i)

print("In the range(5, 3)")
for i in range(5, 3):
    print(i)

print("")
# QUESTION NO.5

print("This program computes the molecular weight of carbohydrates ")
print(",for that Enter the number of atoms of hydrogen,carbon,oxygen ")
h = int(input("Enter the number of hydrogen atoms-: "))
c = int(input("Enter the number of carbon atoms-: "))
o = int(input("Enter the number of oxygen atoms-: "))

weight_of_h = h*1.00794
weight_of_c = c*12.0107
weight_of_o= o*15.99994
print("The moleculer weight of carbohydrate ="
      ,"weight of hydrogen + weight of carbon + weight of oxygen=",end=" ")
print(weight_of_h+weight_of_c+weight_of_o)
