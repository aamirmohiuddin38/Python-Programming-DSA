# Sounds and Delay in python
import os
import time
import winsound

os.system("cls")
print("Python | Programming")
print("----------------------------")
print("Sounds and Delays in Python\n")

for i in range(10):
    winsound.Beep(37+1000*i,200)
    print("\t", i)
    time.sleep(1)

print("\n")