# CCC 2019 Problem J4/S1: Flipper
# Programmer: Foram Gandhi

def flipper():
    line = input()
    grid = ['1', '2', '3', '4']

    for i in line:
        if i == "H":
            temp = grid[0]
            grid[0] = grid[2]
            grid[2] = temp
            temp1 = grid[1]
            grid[1] = grid[3]
            grid[3] = temp1
        else:
            temp = grid[0]
            grid[0] = grid[1]
            grid[1] = temp
            temp1 = grid[2]
            grid[2] = grid[3]
            grid[3]= temp1

    print(grid[0], grid[1])
    print(grid[2], grid[3])
    
flipper()
