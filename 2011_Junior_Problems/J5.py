# CCC 2011 Problem J5: Unfriend
# Programmer: Foram Gandhi

num = int(input())
d = []

for i in range(num-1):
    d.append(input())

def network(n):
    list = []
    for i in range(len(d)):
        if d[i] == str(n):
            list.append(i+1)
    return list

def invites(node, total):
    if network(node) == []:
        return 2
    for i in (network(node)):
        total = (total*invites(i, 1))

    return total + 1

print(invites(num, 1)-1)
