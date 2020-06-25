# CCC 2016 Problem J2: Magic Squares
# Programmer: Foram Gandhi

row = []

def main():
    dimension = 0
    
    while dimension < 4:
        num = input().split()
        num = [int(n) for n in num]
        row.append(num)
        dimension += 1
    
def sums(row):

    sums = 0
    for i in row:
        sums += 1
    return sums
    
def row_column():
    
    s = sums(row[0])
    for r in row:
        if sums(r) != s:
            return "not magic"

    col = []
    for c in range(4):
        col.append(row[c][0])
    s = sums(col)
    
    for i in range(4):
        col1 = []
        for j in range(4):
            col1.append(row[j][i])
        if sums(col1) != s:
            return "not magic"
    return "magic"

main()
print(row_column())
