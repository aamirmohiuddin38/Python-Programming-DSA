# Cricket score status of 2nd Innings of Super Over
import os
os.system("cls")
print("Python | Programming")
print("---------------------------")
print("SUPER OVER: 2nd Innings\n")

runsToWin = int(input("Enter Runs to Win: | "))
balls = 6
ballsLeft = balls
score = 0

ball = 1
while ball <= balls and runsToWin > 0:
    print("\n\n Ball: {:.1}".format(ball/10), end=' ')
    runs = int(input("Enter Runs Score: | "))
    score += runs
    runsToWin -= runs
    ballsLeft -= 1
    avg = score/ball
    if ballsLeft != 0: 
        rr = runsToWin/ballsLeft
    else: 
        rr = float(runsToWin)
    print("\t\t ---------------------------------")
    print("\t\t | SCORE: {} | AVG: {:.2} | RR: {:.2} | ".format(score, avg, rr))
    print("\t\t ---------------------------------")
    if runsToWin > 0:
        print("\t | IND need {} runs to win with {} balls remaining. |".format(runsToWin, ballsLeft))
    ball += 1

if runsToWin <= 0:
    print("\t | IND need 0 runs to win with {} balls remaining. |".format(ballsLeft))
    print("\n IND WIN...")
elif runsToWin == 1:
    print("\n MATCH TIED...")
else:
    print("\n IND LOST THE MATCH")


print("\n")