# Program to print multiplication table of any given number
import os
os.system("cls")

print("Python | Programming")
print("----------------------------")
print("Multiplication Table\n")

num = int(input("Enter num: | "))
limit = int(input("Enter limit: | "))
print("\n\t Mulitiplication Table of | ", num, "| till | ", limit,"|")
print("\t ----------------------------------------------")

for i in range(1, limit+1):
    print("\t {} * {:2} = {:3}".format(num,i,num*i))

print("\n")