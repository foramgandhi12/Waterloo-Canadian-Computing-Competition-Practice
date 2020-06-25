# CCC 2014 Problem J3: Double Dice
# Programmer: Foram Gandhi


antonia = 100
david = 100
rounds = int(input())

count = 0

while count < rounds:
    rolls = input().replace(" ", "")
    a_points = int(rolls[0])
    d_points = int(rolls[1])

    if d_points < a_points:
        david -= a_points
        
    elif a_points < d_points:
        antonia -= d_points
        
    count += 1

print(antonia)
print(david)
        
    
