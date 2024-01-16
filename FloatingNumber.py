# Floating Point Numbers 
import os
import math
os.system("cls")
print("Python | Programming")
print("----------------------------------")
print("float() method - Floating Point Numbers\n")

#scan num
num = input("Enter num: ")

#Displaying Results
print("\tResults...")
print("\t-------------------")
print("\tnum = {}".format(num))
print("\tType = {}".format(type(num)))

print("\n\tConverting to Float:...")
print("\t-----------------------------------")
fnum = float(num)
print("\tfnum = {}".format(fnum))
print("\tType1 = {}".format('%.3f'%fnum))
print("\tType2 = {}".format('%4.2f'%fnum))
print("\tType3 = {}".format('%g'%fnum))
print("\tTypeOfVariable = {}".format(type(fnum)))

#? Int-Float Compatibility
a = 2
fa = 2.0
fb = fa * a
b = fb

print("\n\tInt-Float Compatibility")
print("\t-------------------------------")
print("\t a = {} \t\t| Type(a): {}".format(a, type(a)))
print("\t fa = {}\t| Type(fa): {}".format(fa, type(fa)))
print("\t fb = {}\t| Type(fb): {}".format(fb, type(fb)))
print("\t b = {}\t| Type(b): {}".format(b,type(b)))

#? Floor, Ceil, Round and trunc
print("\n\t TRUNC, FLOOR, CEIL and ROUND")
print("\t------------------------------------")
fVar = 3.1476
print("\t Default fVar = {}".format(fVar))
print("\t Truncated fVar = {}".format(math.trunc(fVar)))
print("\t Floor fVar = {}".format(math.floor(fVar)))
print("\t Ceil fVar = {}".format(math.ceil(fVar)))
print("\t Round fVar = {}".format(round(fVar,2)))

print("\n")