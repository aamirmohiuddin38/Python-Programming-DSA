# Syntax and Examples of For Loop
import os
os.system("cls")
print("Python | Programming")
print("--------------------------------")
print("FOR LOOP")

#? Incrementing by 1 - Ascending Order
print("\n\t Incrementing by 1 - Ascending Order")
print("\t--------------------------------------")
for i in range(0,10):
    print("\t {}".format(i))

#? Incrementing by 2 - Ascending Order
print("\n\t Incrementing by 2 - Ascending Order")
print("\t----------------------------------------")
for i in range(0,10,2):
    print("\t {}".format(i))

#? Decrementing by 1 - Descending Order
print("\n\t Decrementing by 1 - Descending Order")
print("\t ------------------------------------------")
for i in range(10,0, -1):
    print("\t {}".format(i))

#? Decrementing by 2 - Descending Order
print("\n\t Decrementing by 2 - Descending Order")
print("\t-------------------------------------------")
for i in range(10,0,-2):
    print("\t {}".format(i))



print("\n")