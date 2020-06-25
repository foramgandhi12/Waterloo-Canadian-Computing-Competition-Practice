# CCC 2013 Problem J4: Time on task
# Programmer: Foram Gandhi


time = int(input())
num_chores = int(input())

count = 0
num_minutes = []

while count < num_chores:
    
    minutes = int(input())
    num_minutes.append(minutes)
    
    count += 1

num_minutes.sort()
c = 0
total = 0

while total <= time and c < len(num_minutes):
    total += num_minutes[c]
    c += 1

if total > time:
    print(c - 1)
    
else:
    print(count)
