# CCC 2015 Problem J4: Wait Time
# Programmer: Foram Gandhi

def wait_time():
    m = int(input())
    count = 0
    lst = []
    time = -1

    while count < m:
        char = input().split()
        letter = char[0]
        friend = int(char[1])

        if letter == "W":
            time += friend - 1
        
        else:
            time += 1
            visited = False
            val = 0

            while val < len(lst) and not visited:
                if lst[val][0] == friend:
                    visited = True
                else:
                    val += 1

            if letter == "S":
                lst[val][2] = lst[val][2] + (time - lst[val][1])
                lst[val][1] = -1
            elif letter == "R":
                if visited:
                    lst[val][1] = time
                else:
                    lst.append([friend, time, 0])
    
        count += 1

    for i in range(len(lst) - 1):
        for j in range (i + 1, len(lst)):
            if lst[i][0] > lst[j][0]:
                x = lst[i]
                lst[i] = lst[j]
                lst[j] = x

    y = 0
    while y < len(lst):
        if lst[y][1] == -1:
            print(lst[y][0], lst[y][2])
        else:
            print(lst[y][0], -1)
        y += 1
        
wait_time()
