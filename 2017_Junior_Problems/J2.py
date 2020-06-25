# CCC 2017 Problem J2: Shifty Sum
# Programmer: Foram Gandhi

n = int(input())
k = int(input())

shifty_sum = int(n)

for s in range(k):
    n = n * 10
    shifty_sum += n

print(shifty_sum)
    
