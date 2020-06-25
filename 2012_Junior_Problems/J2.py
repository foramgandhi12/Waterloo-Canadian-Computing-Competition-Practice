# CCC 2012 Problem J2: Sounds fishy!
# Programmer: Foram Gandhi

def sounds_fishy():
    
    reading1= int(input())
    reading2= int(input())
    reading3= int(input())
    reading4= int(input())

    if (reading1 < reading2 and reading2 < reading3 and reading3 < reading4):
        print("Fish Rising")
    
    elif (reading2 < reading1 and reading3 < reading2 and reading4 < reading3):
        print("Fish Diving")
    
    elif (reading1 == reading2 and reading2 == reading3 and reading3 == reading4):
        print("Fish at Constant Depth")
    
    else:
        print("No Fish")

sounds_fishy()
