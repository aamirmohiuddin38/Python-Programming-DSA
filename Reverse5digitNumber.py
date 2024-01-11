#Reversing a 5digit Number - Basic BEGINNER LEVEL
import os
os.system("cls")

print("Python | Programming")
print("-----------------------------------------------")
print("Reversing a 5 digit Number - Stepwise (basic: without loops and conditions)\n")

num = int(input("Enter any 5 digit Number: "))
rev = 0

#? Step 1
rem = num % 10
rev = rev + (rem * 10000)
num = int(num / 10)
print("\n\t Step1 -> Quotient: {} | Remainder: {} | Reverse: {}".format(num, rem, rev))

#? Step 2
rem = num % 10
rev = rev + (rem * 1000)
num = int(num / 10)
print("\n\t Step1 -> Quotient: {} | Remainder: {} | Reverse: {}".format(num, rem, rev))

#? Step 3
rem = num % 10
rev = rev + (rem * 100)
num = int(num / 10)
print("\n\t Step1 -> Quotient: {} | Remainder: {} | Reverse: {}".format(num, rem, rev))

#? Step 4
rem = num % 10
rev = rev + (rem * 10)
num = int(num / 10)
print("\n\t Step1 -> Quotient: {} | Remainder: {} | Reverse: {}".format(num, rem, rev))

#? Step 5
rem = num % 10
rev = rev + (rem * 1)
num = int(num / 10)
print("\n\t Step1 -> Quotient: {} | Remainder: {} | Reverse: {}".format(num, rem, rev))

print("\t------------------------------------------------")
print("\t Reversed Number: | {}".format(rev))
print("\t---------------------------------------------\n")
