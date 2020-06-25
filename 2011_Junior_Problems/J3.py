# CCC 2011 Problem J3: Sumac Sequences
# Programmer: Foram Gandhi

def sumac_sequences():
    t1 = int(input())
    t2 = int(input())
    n1 = 0
    n2 = 2

    while t1 >= t2 and t1 >= 0 and t2 >= 0:
        n2 += 1
        n1 = t2
        t2 = t1 - t2
        t1 = n1

    print(n2)
    
sumac_sequences()
