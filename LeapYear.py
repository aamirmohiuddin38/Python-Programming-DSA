# Whether a year is leap year or not
import os
os.system("cls")

print("Python | Programming")
print("----------------------------")
print("Leap Year Program...\n")

year = int(input("Enter num: | "))
print("\t---------------------------------")
if(year % 400 == 0) or ((year % 4 == 0) and (year % 100!= 0)):
    print("\tLeap Year")
else:
    print("\tNot a Leap Year..")
print("\t------------------------------------")


print("\n")