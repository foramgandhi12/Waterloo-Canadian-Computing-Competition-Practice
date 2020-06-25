# CCC 2012 Problem J4: Big Bang Secrets
# Programmer: Foram Gandhi

def big_bang_secrets():
    
    k = int(input())
    word = input()
    l = ""

    for i in range(len(word)):
    
        shift_value = (3 * (i + 1)) + k
        letter = word[i:i+1]

        new = ord(letter) - shift_value

        if new < ord("A"):
            new = ord("Z") + new - ord("A") + 1
        
        l += chr(new)

    print(l)
    
big_bang_secrets()
