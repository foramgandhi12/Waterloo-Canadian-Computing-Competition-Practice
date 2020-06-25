# CCC 2016 Problem J3: Hidden Palindrome
# Programmer: Foram Gandhi

def hidden_palindrome():
    word = input()
    l = []

    for i in range(len(word)):
        for j in range(i, len(word)):
            word1 = [i:j+1]

            if word1 == word1[::-1]:
                l.append(len(word1))
            
    print(sorted(word)[len(l)-1])
    
hidden_palindrome()
