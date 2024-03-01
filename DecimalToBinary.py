# Converting a number from Decimal to Binary
import os
os.system("cls")
print("Python | Programming")
print("------------------------------")
print("Decimal to Binary\n")

num = int(input("Enter num: | "))
print("\n\t Binary Equivalent of {} is: | Bottom to Top -".format(num))
print("\t ----------------------------------------------")
while num is not 0:
    bit = num % 2
    print("\t",bit)
    num = int(num/2)

print(end=" ")