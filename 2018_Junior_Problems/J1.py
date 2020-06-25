# CCC 2018 Problem J1: Telemarketer or not?
# Programmer: Foram Gandhi

def telemarketer():
    lst = []

    for i in range(4):
        num = int(input())
        lst.append(num)

    if (lst[0] == 8 or lst[0] == 9) and (lst[3] == 8 or lst[3] == 9) and (lst[1] == lst[2]):
        print("ignore")
    else:
        print("answer")

telemarketer()
