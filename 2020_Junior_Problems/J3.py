# CCC 2020 Problem J3: Art
# Programmer: Foram Gandhi


n = int(input())
x, y = [], []

for i in range(n):
    xs, ys = input().split(',')
    x.append(int(xs))
    y.append(int(ys))
    
print(f"{min(x) - 1}, {min(y) - 1}")
print(f"{max(x) + 1}, {max(y) + 1}")
