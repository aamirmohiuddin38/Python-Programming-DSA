# Floating Point Numbers 
import os
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

print("\n")