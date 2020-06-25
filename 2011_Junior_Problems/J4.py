# CCC 2011 Problem J4: Boring Business
# Programmer: Foram Gandhi

def boring_business():
    well = {}
    for row in range(-1, -201 -1):
        for col in range(-200, 201):
            well[(row,col)] = False

    well[(-1,0)] = True
    well[(-2,0)] = True
    well[(-3,0)] = True
    well[(-3,1)] = True
    well[(-3,2)] = True
    well[(-3,3)] = True
    well[(-4,3)] = True
    well[(-5,3)] = True
    well[(-5,4)] = True
    well[(-5,5)] = True
    well[(-4,5)] = True
    well[(-3,5)] = True
    well[(-3,6)] = True
    well[(-3,7)] = True
    well[(-4,7)] = True
    well[(-5,7)] = True
    well[(-6,7)] = True
    well[(-7,7)] = True
    well[(-7,6)] = True
    well[(-7,5)] = True
    well[(-7,4)] = True
    well[(-7,3)] = True
    well[(-7,2)] = True
    well[(-7,1)] = True
    well[(-7,0)] = True
    well[(-7,-1)] = True
    well[(-6,-1)] = True
    well[(-5,-1)] = True


    drill_command = input()
    strip_command = drill_command.replace(" ", "")
    direction = strip_command[0]
    length = int(strip_command[1])

    tf = True
    row = -5
    col = -1

    while tf and direction != "q":
        dr = 0
        dc = 0

        if direction == "d":
            dr = -1
        elif direction == "u":
            dr = 1
        elif direction == "l":
            dc = -1
        elif direction == "r":
            dc = 1

        while length > 0:
            row += dr
            col += dc

            if well[(row,col)]:
                tf = False
            else:
                well[(row,col)] = True
            
            distance -= 1

        if tf:
            print(col, row, "safe")
        else:
            print(col, row, "DANGER")

        drill_command = input()
        strip_command = drill_command.replace(" ", "")
        direction = strip_command[0]
        length = int(strip_command[1])
      
boring_business()
