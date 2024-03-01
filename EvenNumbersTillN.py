# WHILE LOOP - Printing sum of Even numbers upto n
import os
os.system("cls")
print("Python | Programming")
print("---------------------------")
print("EVEN Numbers till N\n")

N = int(input("Enter n: | "))
num = 0
sum = 0
print("\n\t Sum of Even Numbers till: | ", N)
print("\t ----------------------------------")
while num <= N:
    if num%2 == 0:
        sum += num
        print("\t Sum: {:3} | {:3} ".format(num, sum))
    num += 1

print(end=" ")