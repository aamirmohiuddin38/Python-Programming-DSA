# Program to Calculate circle Parameters - Circumference and Area
import os
import constants as const
os.system("cls")

print("Python | Programming")
print("------------------------------------")
print("Circle Parameters - Circumference and Area")

rad = float(input("\nEnter the Radius: "))
dia = 2 * rad
cir = 2 * const.PI * rad
area = const.PI * rad * rad

#display results
print("\t Circle - Circumference and Area")
print("\t -----------------------------------")
print("\t Radius:\t| {}".format('%8.2f'%rad))
print("\t Diameter:\t| {}".format('%8.2f'%dia))
print("\t Circumference:\t| {}".format('%8.2f'%cir))
print("\t Area:\t\t| {}".format('%8.2f'%area))

print("\n")
