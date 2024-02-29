# Printing Pattern 1
import os
os.system("cls")
print("Python | Programming")
print("---------------------------")
print("Pattern 2\n")

for row in range(10,0,-1):
    for col in range(0,row):
        print("*", end=" ")
    print(" ")

print("\n")