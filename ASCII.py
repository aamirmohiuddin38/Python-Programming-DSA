# Program to print ascii values of alphabets
import os
os.system("cls")

print("Python | Programming")
print("------------------------------")
print("ASCII/UNICODE Values")

print("\n\t ASCII/UNICODE Values of a-z")
print("\t --------------------------------")
for i in range(ord('a'), ord('z')+1):
    print("\t ", chr(i)," | ", i)

print("\n\t ASCII/UNICODE Values of A-Z")
print("\t --------------------------------")
for i in range(ord('A'), ord('Z')+1):
    print("\t ", chr(i)," | ", i)

"""The term "ord" is short for "ordinal", which refers to the position or
order of something in a series. In the context of programming, particularly 
in Python, the ord() function is used to obtain the Unicode code point 
(an integer representing the position of a character in the Unicode standard)
of a given character.
For example, the ordinal value of the character 'A' is 65, as per the ASCII 
and Unicode standards. So, ord('A') would return 65."""