# Program to swap values of two variables without using a third variable
import os
os.system("cls")

print("Python | Programming")
print("---------------------------------")
print("Swap Without Using temp Program\n")

num1 = int(input("Enter the First Number(num1): "))
num2 = int(input("Enter the Second Number(num2): "))

#Before swapping
print("\n\t Before Swapping...")
print("\t------------------------------")
print("\tFirst Number (num1): | {}".format(num1))
print("\tSecond Number (num2): | {}\n".format(num2))

#Swapping
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

#After swapping
print("\n\t After Swapping...")
print("\t------------------------------")
print("\tFirst Number (num1): | {}".format(num1))
print("\tSecond Number (num2): | {}\n".format(num2))