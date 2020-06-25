# CCC 2016 Problem J5: Tandem Bicycle
# Programmer: Foram Gandhi

def tandem_bicycle():
    question = int(input())
    pairs = int(input())

    d_speed = input().split(" ")
    p_speed = input().split(" ")

    dmojistan_speed = [int(x) for s in d_speed]
    pegland_speed = [int(x) for s in p_speed]

    if question == 1:
        dmojistan_speed.sort()
        pegland_speed.sort()
    
        total_speed = 0
        for t in range(pairs):
            total_speed += max(dmojistan_speed[t], pegland_speed[t])
        print(total_speed)


    elif question == 2:
        dmojistan_speed.sort()
        pegland_speed.sort(reverse = True)
    
        total_speed = 0
        for t in range(pairs):
            total_speed += max(dmojistan_speed[t], pegland_speed[t])
        print(total_speed)
        
tandem_bicycle()
