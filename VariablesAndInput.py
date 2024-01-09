import os
os.system('cls')

print("Python | Programming")
print("--------------------------------")
print("Variables and input Object\n")

#Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
# Scanning values from user - using input()

str = input("Enter any Number:")
intNum = int(input("Enter any Integer Number:"))
floatNum = float(input("Enter any float Number:"))

print("\tResults:....")
print("\t---------------------")
print("\tstr = {} | type = {}".format(str, type(str)))
print("\tintNum = {} | type = {}".format(intNum, type(intNum)))
print("\tfloatNum = {} | type = {}\n".format(floatNum, type(floatNum)))