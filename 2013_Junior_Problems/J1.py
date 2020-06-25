# CCC 2013 Problem J1: Next in line
# Programmer: Foram Gandhi


def next_in_line():
  youngest = int(input())
  middle = int(input())

  if 0 <= youngest <= 50 and 0 <= middle <= 50:
      oldest = middle + (middle - youngest)
      print(oldest)

  else:
      print("Try again.")

next_in_line()
