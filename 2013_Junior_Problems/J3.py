# CCC 2013 Problem J3: From 1987 to 2013
# Programmer: Foram Gandhi


def distinct(year):
    
    starting_year = str(year)

    count = 0
    
    while count < len(starting_year):
        if starting_year.count(starting_year[count]) > 1:
            return False
        count += 1
        
    return True


next_year = int(input()) + 1

while not distinct(next_year):
    next_year += 1
    
print(next_year)
