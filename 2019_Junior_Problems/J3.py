# CCC 2019 Problem J3: Cold Compress
# Programmer: Foram Gandhi


def num_firsts(line):
    start = line[0]
    count = 0
    
    while count < len(line) and start == line[count]:
        count += 1
    return count

def encode(message):
    output = ""
    count = 0

    while count < len(message):
        num = num_firsts(message[count:])
        output += str(num) + " " + str(message[count]) + " "
        count += num
        
    print(output)

n = int(input())
counter = 0

while counter < n:
    inp = input()
    encode(inp)
    counter += 1

