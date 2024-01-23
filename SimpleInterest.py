#Program to calculate simple interest
import os
os.system("cls")

print("Python | Programming")
print("------------------------------")
print("Simple Interest Program\n")

principle = float(input("Enter Principle: "))
rate = float(input("Rate of interest: "))
time = float(input("Time(years): "))

si = principle * rate * time / 100
tds = 0.1 * si
amount = principle + si - tds

#? Display results
print("\t --------------------------------")
print("\t Simple Interest....")
print("\t --------------------------------")
print("\t Principle: \t\t| {}".format('%8.0f'%principle))
print("\t Rate Of Interest: \t| {}".format('%8.0f'%rate))
print("\t Time in years: \t| {}".format('%8.0f'%time))
print("\t Interest Before Tax: \t| {}".format('%8.0f'%si))
print("\t TDS(10% of Interest): \t| {}".format('%8.0f'%tds))
print("\t Interest After Tax: \t| {}".format('%8.0f'%(si-tds)))
print("\t ---------------------------------")
print("\t Final Amount: \t\t| {}".format('%8.0f'%amount))
print("\t ---------------------------------")