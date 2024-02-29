# Printing Pattern 1
import os
os.system("cls")
print("Python | Programming")
print("---------------------------")
print("Pattern 1\n")

for row in range(10):
    for col in range(0,row+1):
        print("*", end=" ")
    print(" ")

print("\n")