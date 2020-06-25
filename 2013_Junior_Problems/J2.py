# CCC 2013 Problem J2: Rotating letters
# Programmer: Foram Gandhi


word = input()
rotating_letters = "IOSHZXN"

count = 0

for letter in word:
    if letter in rotating_letters:
        count += 1

if count == len(word):
    print("YES")
else:
    print("NO")
