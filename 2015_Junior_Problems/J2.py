# CCC 2015 Problem J2: Happy or Sad
# Programmer: Foram Gandhi


message = str(input())

if message.count(':-)') == 0 or message.count(':-(') == 0:
    print("none")
elif message.count(':-)') == message.count(':-('):
    print("unsure")
elif message.count(':-)') > message.count(':-('):
    print("happy")
elif message.count(':-)') < message.count(':-('):
    print("sad")

