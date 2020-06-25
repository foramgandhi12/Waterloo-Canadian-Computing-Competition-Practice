# CCC 2016 Problem J4: Arrival Time
# Programmer: Foram Gandhi

def arrival_time():
    departure = input().split(":")
    hour = int(departure[0]) * 60
    minute = int(departure[1])
    departure = hour + minute
    arrival = int(departure)
    num = 0

    for i in range(departure, departure + 120):
        if (arrival >= 900 and arrival < 1140) or (arrival >= 420 and arrival < 600):
            arrival += 2
        else:
            arrival += 1
        if arrival == 1440:
            arrival = 0
        
    while arrival >= 60:
        arrival -= 60
        num += 1
        if arrival < 60:
            break

    minute = arrival

    if minute < 10:
        minute = '0' + str(minute)

    if num < 10:
        num = '0' + str(num)

    print(str(num) + ":" + str(minute))
    
arrival_time()
