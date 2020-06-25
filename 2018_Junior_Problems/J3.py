# CCC 2018 Problem J3: Are we there yet?
# Programmer: Foram Gandhi


distances = input().split(" ")
distances = [int(i) for i in distances]

def sum_left(x, y):
    count = 0
    for i in range(x - 1, y - 1, -1):
        count += distances[i]
        
    return count

def sum_right(x, y):
    count = 0
    for i in range(x, y):
        count += distances[i]
        
    return count

for i in range(0, 5):
    row = ""
    
    for j in range(0, 5):
        if i < j:
            row += str(sum_right(i, j)) + " "
        elif i > j:
            row += str(sum_left(i, j)) + " "
        elif i == j:
            row += "0 "
            
    print(row)
