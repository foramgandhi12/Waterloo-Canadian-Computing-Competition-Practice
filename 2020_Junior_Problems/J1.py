# CCC 2020 Problem J1: Dog Treats
# Programmer: Foram Gandhi


def dog_treats():
    
    s = int(input())
    m = int(input())
    l = int(input())

    happiness_score = (1 * s) + (2 * m) + (3 * l)

    if happiness_score >= 10:
        print("happy")
    else:
        print("sad")

dog_treats()
