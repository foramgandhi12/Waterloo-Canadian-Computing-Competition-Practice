# CCC 2020 Problem J4: Cyclic Shifts
# Programmer: Foram Gandhi

def cyclic_shifts():
    t = input()
    s = input()
    lst = []
    tf = "no"

    for i in range(len(s)):
        if s in t:
            tf = "yes"
            break
        s = s[-1] + s[:-1]
    
    print(tf)
    
cyclic_shifts()
