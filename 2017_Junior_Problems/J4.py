# CCC 2017 Problem J4: Favourite Times
# Programmer: Foram Gandhi


d = int(input())

def s_time(hour, minute, str_time, val):
    
    for i in range(d + 1):
        str_time = ''
        if minute < 9:
            str_time += str(hour)
            minute += 1
            str_time += str(0) + str(minute)
            
        elif minute == 59:
            hour = choose_hour(hour)
            str_time += str(hour)
            str_time += '00'
            minute = 1
            
        else:
            str_time += str(hour)
            minute += 1
            str_time += str(minute)
            
        if arithmetic(str_time):
            val += 1
            
    return val

def arithmetic(str_time):
    if len(str_time) == 4:
        diff = int(str_time[1]) - int(str_time[0])
        diff1 = int(str_time[2]) - int(str_time[1])
        diff2 = int(str_time[3]) - int(str_time[2])

        if diff == diff1 == diff2:
            return True

    else:
        diff = int(str_time[1]) - int(str_time[0])
        diff1 = int(str_time[2]) - int(str_time[1])

        if diff == diff1:
            return True

def choose_hour(hour):
    if hour == 11:
        return 12
    if hour == 12:
        return 1
    else:
        return hour + 1

print(s_time(12, 0, "", 0))
