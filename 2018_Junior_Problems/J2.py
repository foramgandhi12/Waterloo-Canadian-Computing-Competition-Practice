# CCC 2018 Problem J2: Occupy Parking
# Programmer: Foram Gandhi


n = int(input())
yesterday = input()
today = input()

tf = 0
for i in range(len(yesterday)):
    if yesterday[i] == "C" and today[i] == "C":
        tf += 1

print(tf)
