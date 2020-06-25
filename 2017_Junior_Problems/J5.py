# CCC 2017 Problem J5: Nailed It!
# Programmer: Foram Gandhi


n = int(input())
lst = input().split()
lst = [int(i) for i in lst]
    
d = [0] * 4002
m = [0] * 2001

for i in lst:
    m[i] += 1

for i in range(1, 2001):
    for j in range(i, 2001):
        
        if i == j:
            d[i + j] += m[i]/2
        else:
            d[i + j] += min(m[i], m[j])
            
    h = 0
    for i in d:
        if i > h:
            h = i
    f = 0
    for i in d:
        if i == h:
            f += 1
print(h, f)
