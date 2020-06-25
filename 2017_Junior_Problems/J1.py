# CCC 2017 Problem J1: Quadrant Selection
# Programmer: Foram Gandhi


x = int(input())
y = int(input())

def quadrant_selection(x, y):

    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    else:
        print("4")

quadrant_selection(x, y)
