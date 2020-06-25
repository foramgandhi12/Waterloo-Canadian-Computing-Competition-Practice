# CCC 2014 Problem J1: Triangle Times
# Programmer: Foram Gandhi

def triangle_times():
  int1 = int(input())
  int2 = int(input())
  int3 = int(input())

  sum_int = int1 + int2 + int3

  if int1 == 60 and int2 == 60 and int3 == 60:
      print("Equilateral")
    
  elif sum_int == 180 and int1 == int2 or int1 == int3 or int2 == int3:
      print("Scalene")

  elif sum_int != 180:
      print("Error")

  else:
      print("Scalene")
      
triangle_times()
