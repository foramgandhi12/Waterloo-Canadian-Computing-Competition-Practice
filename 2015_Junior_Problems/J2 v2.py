# CCC 2015 Problem J2 v2: Happy or Sad
# Programmer: Foram Gandhi


message = str(input())
h = 0
s = 0

for i in range(len(message) - 2):
    if message[i:i+3] == ":-)":
        h += 1
    elif message[i:i+3] == ":-(":
        s += 1

if h == 0 or s == 0:
    print("none")
elif h > s:
    print("happy")
elif h < s:
    print("sad")
else:
    print("unsure")
