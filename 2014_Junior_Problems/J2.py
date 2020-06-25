# CCC 2014 Problem J2: Vote Count
# Programmer: Foram Gandhi

def vote_count():
    votes = int(input())
    singer= input()

    a_count = 0
    b_count = 0

    for letter in singer:
        if letter == 'A':
            a_count += 1
        elif letter == 'B':
            b_count += 1

    if a_count > b_count:
        print("A")

    elif b_count > a_count:
        print("B")

    else:
        print("Tie")
        
vote_count()
