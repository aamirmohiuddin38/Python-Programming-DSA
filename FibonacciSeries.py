#Generating a Fibonacci Series till given max value
import os
os.system("cls")
print("Python | Programming")
print("-----------------------------")
print("Fibonacci Series\n")

limit = int(input("Enter max value: | "))
a = 0
b = 1
print("\n\t Fibonacci Series upto or less than : | {}".format(limit))
print("\t -----------------------------------------")
print("\t 0, 1,", end = ' ')
c = a + b
while c <= limit:
    print(c, end=", ")
    a, b = b, c
    c = a + b

print("\n")