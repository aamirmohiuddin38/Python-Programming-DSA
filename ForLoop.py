# Syntax and Examples of For Loop
import os
os.system("cls")
print("Python | Programming")
print("--------------------------------")
print("FOR LOOP")

#! Iterating as Int

#? Incrementing by 1 - Ascending Order
print("\n\t Incrementing by 1 - Ascending Order")
print("\t--------------------------------------")
for i in range(0,10):
    print("\t",i)

#? Incrementing by 2 - Ascending Order
print("\n\t Incrementing by 2 - Ascending Order")
print("\t----------------------------------------")
for i in range(0,10,2):
    print("\t",i)

#? Decrementing by 1 - Descending Order
print("\n\t Decrementing by 1 - Descending Order")
print("\t ------------------------------------------")
for i in range(10,0, -1):
    print("\t",i)

#? Decrementing by 2 - Descending Order
print("\n\t Decrementing by 2 - Descending Order")
print("\t-------------------------------------------")
for i in range(10,0,-2):
    print("\t",i)

#! for in range(a,b,step) - 'a' is included and 'b' is not
#? Syntax to print numbers on same line
print("\n\t Print numbers of same line...")
print("\t---------------------------------------")
print("\t", end ='')
for i in range(0,10):
    print(i , end = " ")

#! Iterating as Float
#? Incrementing by 0.1 - Ascending Order
"""The range() function doesn't support floating-point numbers for its step argument.
However, you can achieve the desired result by using a while loop instead."""

print("\n\n\t Incrementing by 0.1 - Ascending Order")
print("\t-------------------------------------------")
i = 0.0
while(i<=1.0):
    print("\t {:.1f}".format(i))
    i += 0.1

print("\n\n\t Incrementing by 0.05 - Ascending Order")
print("\t-------------------------------------------")
i = 0.0
while(i<=1.0):
    print("\t {:.2f}".format(i))
    i += 0.05

print("\n\n\t Decrementing by 0.05 - Ascending Order")
print("\t-------------------------------------------")
i = 1.0
while(i>=0):
    print("\t {:.2f}".format(i))
    i -= 0.05

print("\n\t a-z alphabets....")
print("\t--------------------------")
for i in range(ord('a'), ord('z')):
    print("\t",chr(i))

print("\n\t A-Z alphabets....")
print("\t--------------------------")
for i in range(ord('A'), ord('Z')):
    print("\t",chr(i))

print("\n")