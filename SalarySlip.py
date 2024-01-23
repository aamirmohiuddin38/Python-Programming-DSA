#Program to generate Salary slip
import os
os.system("cls")

print("Python | Programming")
print("------------------------------")
print("Salary Slip of an Employee..\n")

basic = float(input("Enter Basic: "))

#? calculations
da = 0.1 * basic #10% of basic
hra = 0.5 * basic + da #50% of basic + da
conveyance = 1600 #fixed
medical = 1250 #fixed
gross = basic + da + hra + conveyance + medical

#?deductions
esic = 0.0475 * gross #4.75% of gross
pf = 0.12 * basic #12% of gross
netPreTax = gross - esic - pf
tds = 0.05 * netPreTax
finalSalary = netPreTax - tds

#?display
print("\n\t ----------------------------------")
print("\t Basic Salary : \t {}".format('%8.0f'%basic))
print("\t ----------------------------------")
print("\t Basic: \t\t| {}".format('%8.0f'%basic))
print("\t DA: \t\t\t| {}".format('%8.0f'%da))
print("\t HRA: \t\t\t| {}".format('%8.0f'%hra))
print("\t Conveyance: \t\t| {}".format('%8.0f'%conveyance))
print("\t Medical: \t\t| {}".format('%8.0f'%medical))
print("\t Gross Salary: \t\t| {}".format('%8.0f'%gross))
print("\t ESIC: \t\t\t| {}".format('%8.0f'%esic))
print("\t Provident Fund: \t| {}".format('%8.0f'%pf))
print("\t Net Before Tax: \t| {}".format('%8.0f'%netPreTax))
print("\t TDS: \t\t\t| {}".format('%8.0f'%tds))
print("\t ----------------------------------")
print("\t Salary in Hand: \t| {}".format('%8.0f'%finalSalary))
print("\t ----------------------------------")