# CCC 2019 Problem J2: Time to Decompress
# Programmer: Foram Gandhi

def time_to_decompress():
    l = int(input())
    count = 0
    lst = []

    while count < l:
        line = input().split(" ")
        lst.append(line)
        count += 1

    for i in range(len(lst)):
        print(lst[i][1] * int(lst[i][0]))
        
time_to_decompress()
