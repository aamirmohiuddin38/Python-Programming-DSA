# Reverse a number of any number of digits
import os
os.system("cls")
print("Python | Programming")
print("---------------------------")
print("REVERSE NUMBER\n")

num = int(input("Enter num: | "))
temp = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rem + (rev*10)
    num = int(num/10)

print("\n\t Reverse of {} is: | {}".format(temp, rev))
print("\t--------------------------------")

if temp == rev:
    print("\tIt is PALINDROME")
else:
    print("\tNOT A PALINDROME")

print(end=" ")