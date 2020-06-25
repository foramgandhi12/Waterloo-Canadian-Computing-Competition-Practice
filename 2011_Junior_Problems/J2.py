# CCC 2011 Problem J2: Who Has Seen The Wind
# Programmer: Foram Gandhi

def wind():
    h = int(input())
    max_hours = int(input())

    t = 1
    altitude = (-6*t*t*t*t) + (h*t*t*t) + (2*t*t) + t

    while altitude > 0 and t < max_hours:
        t += 1
        altitude = (-6*t*t*t*t) + (h*t*t*t) + (2*t*t) + t
    
    if altitude <= 0:
        print("The balloon first touches ground at hour:\n", t)

    else:
        print("The balloon does not touch ground in the given time.")

wind()
