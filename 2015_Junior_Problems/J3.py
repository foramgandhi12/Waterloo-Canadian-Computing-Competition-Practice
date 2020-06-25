# CCC 2015 Problem J3: Rovarspraket
# Programmer: Foram Gandhi


word = input("")
wordLow = word.lower()

closestVowel = "aaeeeiiiiooooouuuuuuu"                                                
consonant = "bcdfghjklmnpqrstvwxyz"                                                  
nextConsonant = "cdfghjklmnpqrstvwxyzz"                                          
newWord = ""                                                                      

for i in range(len(wordLow)):
    j = consonant.find(wordLow[i])    #stores the index of the first occurrence of i in the word entered by the user
    newWord = newWord + wordLow[i]    #stores the original letter 
    
    if j > -1:
        newWord = newWord + closestVowel[j] + nextConsonant[j]    #adds the closest vowel and next consonant in terms of j
        
print(newWord)
