# CCC 2019 Problem J1: Winning Score
# Programmer: Foram Gandhi


def winning_score():
    count = 0
    lst = []

    while count < 6:
        scoring = input()
        lst.append(int(scoring))
        count += 1
    
    apple_score = (lst[0] * 3) + (lst[1] * 2) + (lst[2] * 1)
    banana_score = (lst[3] * 3) + (lst[4] * 2) + (lst[5] * 1)

    if apple_score > banana_score:
        print("A")
    elif banana_score > apple_score:
        print("B")
    else:
        print("T")

winning_score()
