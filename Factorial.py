# To calculate the factorial of a number
import os
os.system("cls")
print("Python | Programming")
print("-----------------------------")
print("Factorial of a Number\n")

fact = 1
num = int(input("Enter num: | "))
temp = num

if num == 0:
    print("\n\t Factorial of {} is: | {}".format(num, fact))
else:
    while num is not 0:
        fact = fact * num
        num -= 1
    print("\n\t Factorial of {} is: | {}".format(temp, fact))

print()