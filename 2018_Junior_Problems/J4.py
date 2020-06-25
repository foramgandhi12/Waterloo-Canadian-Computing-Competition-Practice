# CCC 2018 Problem J4: Sunflowers
# Programmer: Foram Gandhi

n = int(input())
lst = []
count = 0

while True:
    lst1 = []
    while count < n:
        line = input()
        lst1 = [int(i) for i in line.split(" ")]
        lst.append(lst1)
        count += 1
    break
    
def rotate(arr):
    temp = []
    for i in range(len(arr)):
        temp1 = []
        for j in range(len(arr)):
            temp1.append(0)
        temp.append(temp1)

    for row in range(len(arr)):
        col = len(arr) - 1
        origin = 0
        while col >= 0 and origin < len(arr):
            temp[row][origin] = arr[col][row]
            origin += 1
            col -= 1

    return temp

def check(lst):
    tf = False
    for a in range(len(lst)):
        if lst[a] != sorted(lst[a]):
            tf = True

    temp1 = []
    for l in range(len(lst)):
        temp1.append(lst[l][0])

    if temp1 != sorted(temp1):
        tf = True

    if tf:
        return True
    elif not tf:
        return False

while True:
    if not check(lst):
        k = lst
        break
    else:
        lst = rotate(lst)

for i in k:
    string = ""
    for j in i:
        string += str(j) + " "
    print(string)
