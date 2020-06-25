# CCC 2014 Problem J5: Assigning Partners
# Programmer: Foram Gandhi

def assigning_partners():
    num_students = int(input())
    first_names = input().split()
    order_names = input().split()

    tf = True
    count = 0

    for name in range(num_students):

        j = first_names.index(order_names[name]) # returns index of first name in second list
    
        if order_names[j] != first_names[name] or j == name:
            tf = False

    if tf:
        print("good")
    else:
        print("bad")
        
assigning_partners()
