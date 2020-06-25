# CCC 2012 Problem J3: Icon Scaling
# Programmer: Foram Gandhi


factor = int(input())

count = 0
for count in range(factor):
    print(("*" * factor) + ("X" * factor) + ("*" * factor))
    count += 1

i = 0
for i in range(factor):
    print((" " * factor) + ("X" * (factor * 2)))
    i += 1

j = 0
for j in range(factor):
    print(("*" * factor) + (" " * factor) + ("*" * factor))
    j += 1
