# CCC 2015 Problem J1: Special Day
# Programmer: Foram Gandhi


def special_day():
  month = int(input())
  day = int(input())

  if month < 2 or (month == 2 and day < 18):
      print("Before")
  elif month == 2 and day == 18:
      print("Special")
  else:
      print("After")

special_day()
