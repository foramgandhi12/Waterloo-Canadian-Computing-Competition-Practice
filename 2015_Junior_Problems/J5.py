# CCC 2015 Problem J5: Pi-Day
# Programmer: Foram Gandhi


pieces = int(input())
people = int(input())

dct = {}

def pi_day(n, k, minimum):
    
    if k == 1 or n == k:
        return 1
            
    if (n, k, minimum) in dct:
        return dct[(n, k, minimum)]

    t = 0
    for i in range(minimum, n / k + 1):
        t += pi_day(n - i, k - 1, i)
                
    dct[(n, k, minimum)] = t
            
    return t

print(pi_day(pieces, people, 1))
