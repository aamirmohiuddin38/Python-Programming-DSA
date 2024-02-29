# Pattern 4: Pyramid Pattern
import os
os.system("cls")
print("Python | Programming")
print("------------------------")
print("Pyramid Pattern - 4\n")

spaces = 10
for row in range(10):
    for space in range(spaces):
        print(end=" ")
    for star in range(row):
        print("*", end=' ')
    print(" ")
    spaces -= 1
