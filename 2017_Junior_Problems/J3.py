# CCC 2017 Problem J3: Exactly Electrical
# Programmer: Foram Gandhi


start_coord = input().split()
x1 = int(start_coord[0])
y1 = int(start_coord[1])

dest_coord = input().split()
x2 = int(dest_coord[0])
y2 = int(dest_coord[1])

battery_charge = int(input())

shortest_path = abs(x1 - x2) + abs(y1 - y2)

if battery_charge >= shortest_path:
    if (battery_charge - shortest_path) % 2 == 0:
        print("Y")
    else:
        print("N")
else:
    print("N")
