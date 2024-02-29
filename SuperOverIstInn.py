# Cricket Score status of first Innings of Super Over
import os
os.system("cls")

print("Python | Programming")
print("------------------------------")
print("SUPER OVER - Ist Innings")

balls = 0.6
score = 0
max = 0

ball = 0.1
while ball <= balls:
    print("\n\n Ball: {:.1} |".format(ball), end = ' ')
    runs = int(input("Enter runs scored: "))
    score += runs
    if runs > max: max = runs
    avg = score/(ball*10)
    print("\t -------------------------------")
    print("\t | SCORE: {} | AVG: {:.2} | Max: {} |".format(score, avg, max))
    print("\t -------------------------------")
    ball += 0.1

print("\n\t RUNS TO WIN: ", score + 1)
print("\n")
