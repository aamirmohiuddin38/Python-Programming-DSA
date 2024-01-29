# Decision Making - IF ELSE ELIF
import os
os.system("cls")

print("Python | Programming")
print("--------------------------------------")
print("Decision Making Statements....\n")

a = int(input("Enter a: | "))

#? IF STATEMENT - checking whether 'a' is even, if even, print 'a' and if not then do nothing
print("\n\t -----------------------------------")
print("\t If(): Statement...")
print("\t -----------------------------------")
if(a % 2 == 0):
    print("\t 'a' is EVEN.")

#?IF - ELSE STATEMENT - checking whether 'a' is even or odd
print("\n\t ------------------------------")
print("\t IF-ELSE Statement...")
print("\t ------------------------------")
if (a % 2 == 0):
    print("\t 'a' is EVEN")
else:
    print("\t 'a' is ODD")

print("\n")