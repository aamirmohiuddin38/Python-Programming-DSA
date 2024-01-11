# Program to find sum and Average of 3 numbers - BEGINNER
import os
os.system("cls")

print("Python | Programming")
print("--------------------------------")
print("Sum and Average Program\n")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

sum = num1 + num2 + num3
avg = sum/3

print("\n\tResults:.... ")
print("\t------------------------------------")
print("\tGiven Numbers: | {}, {}, {}".format(num1, num2, num3))
print("\tSum: | {}".format(sum))
print("\tAverage: | {}\n".format(avg))
