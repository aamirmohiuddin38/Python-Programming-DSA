# Menu Driven Calc till user exits
import os
os.system("cls")

print("Python | Programming")
print("----------------------------")
print("Menu Driven Calc...\n")

repeat = True
while(repeat):
    num1 = int(input("\nEnter num1: | "))
    num2 = int(input("Enter num2: | "))

    #choices
    print("\n\t-------------------------")
    print("\t Choose Option: ")
    print("\t-------------------------")
    print("\t 1. Add")
    print("\t 2. Subtract")
    print("\t 3. Multiply")
    print("\t 4. Divide")
    print("\t 5. Exit")
    print("\t--------------------------")
    choice = input("\tEnter choice: | ")

    #calculation
    print("\t ---------------------------")
    if(choice == '1'):print("\t Result | num1 + num2 = {}".format(num1 + num2))
    elif (choice == '2'):print("\t Result | num1 - num2 = {}".format( num1 - num2))
    elif (choice == '3'):print("\t Result | num1 * num2 = {}".format( num1 * num2))
    elif (choice == '4'):print("\t Result | \n\t num1 / num2 (quotient) = {} \n\t num1 % num2 (remaidner) = {}".format(num1 / num2, num1 % num2))
    elif (choice == '5'):print("\t Thank You....\n")
    else: print("\t Invalid Option.. \n")
    print("\t -----------------------------\n")

    repeat = int(input("\nREPEAT? 1-YES, 0-N0: | "))

print("\n")