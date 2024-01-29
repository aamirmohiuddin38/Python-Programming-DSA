# Decision Making - IF ELSE ELIF
import os
os.system("cls")

print("Python | Programming")
print("--------------------------------------")
print("Decision Making Statements....\n")

a = int(input("Enter a: | "))
b = int(input("Enter b: | "))

#? IF STATEMENT - checking whether 'a' is even, if even, print 'a' and if not then do nothing
print("\n\t -----------------------------------")
print("\t If(): Statement...")
print("\t -----------------------------------")
if(a % 2 == 0):
    print("\t 'a' is EVEN.")

#?IF - ELSE STATEMENT - checking whether 'a' is even or odd
print("\n\t ------------------------------")
print("\t IF-ELSE Statement...")
print("\t ------------------------------")
if (a % 2 == 0):
    print("\t 'a' is EVEN")
else:
    print("\t 'a' is ODD")

#?IF - ELSE IF-ELSE STATEMENT - comparing two numbers whether they are less, greater or equal
print("\n\t ------------------------------")
print("\t IF-ELIF-ELSE Statement...")
print("\t ------------------------------")
if a>b:
    print("\t 'a' is GREATER")
elif a == b:
    print("\t 'a' and 'b' are equal")
else:
    print("\t 'b' is GREATER")

#?IF - ELSE STATEMENT - ONE LINER
print("\n\t ------------------------------")
print("\t ONELINER IF-ELIF Statement...")
print("\t ------------------------------")
if a%2==0: print("\t 'a' is EVEN")
else: print("\t 'a' is ODD")

#? TERNARY IF ELSE Statement....
print("\n\t ------------------------------")
print("\t TERNERY IF...")
print("\t ------------------------------")
max = a if a>b else b
print("\t max = {}".format(max))
print("\t max is {}".format(a)) if a > b else print("\t max is {}".format(b))

#?IF - ELSE IF-ELSE STATEMENT - comparing two numbers whether they are less, greater or equal
print("\n\t ------------------------------")
print("\t IF-ELSE | Comparison Operators")
print("\t ------------------------------")
if(a<b): print("\t a<b is true")
if(a<=b): print("\t a<=b is true")
if(a==b): print("\t a==b is true")
if(a>b): print("\t a>b is true")
if(a>=b): print("\t a>=b is true")
if(a!=b): print("\t a!=b is true")

''' When PYTHON DOES ANY OF THE ABOVE COMPARISONS, IT RETURNS A "True(NON ZERO)", if the condition is true and "FALSE(0)" if the condition
    is false'''

#?IF - ELSE Combining Multiple Conditions
print("\n\t ------------------------------")
print("\t IF-ELSE | Combining multiple conditions...")
print("\t ------------------------------")
if(a<100 and a%2==0) : print("\t a < 100 and even") #both conditions must be true - AND
if(a<100 or a%2==0): print("\t a is either less than 100 or even") #either of the condition must be true - OR

print("\n")