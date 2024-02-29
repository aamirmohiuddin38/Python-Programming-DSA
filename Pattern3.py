# Printing Pattern 1
import os
os.system("cls")
print("Python | Programming")
print("---------------------------")
print("Multiple Patterns - 3\n")

for row in range(10):
    for col in range(0,row+1):
        if row == col: print(">", end=" ")
        else: print("*", end = ' ')
    print(" ")

for row in range(9,0,-1):
    for col in range(1,row+1):
        if row == col: print(">", end=" ")
        else: print("*", end=" ")
    print(" ")

print("\n")