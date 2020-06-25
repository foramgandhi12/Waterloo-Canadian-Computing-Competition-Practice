# CCC 2012 Problem J1: Speed fines are not fine!
# Programmer: Foram Gandhi

def speed_fines():
  speed_limit = int(input("Enter the speed limit: "))
  recorded_speed = int(input("Enter the recorded speed of the car: "))

  difference = recorded_speed - speed_limit

  if recorded_speed <= speed_limit:
      print("Congratulations, you are within the speed limit!")
    
  elif difference >= 1 and difference <= 20:
      print("You are speeding and your fine is $100.")
    
  elif difference >= 21 and difference <= 23:
      print("You are speeding and your fine is $270.")
    
  elif difference >= 31:
      print("You are speeding and your fine is $500.")
      
speed_fines()
