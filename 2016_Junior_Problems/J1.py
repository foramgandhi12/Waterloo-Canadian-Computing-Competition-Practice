# CCC 2016 Problem J1: Tournament Selection
# Programmer: Foram Gandhi

def tournament_selection():
  games = 0
  outcome = []

  while games < 6:
      win_loss = input()
      outcome.append(win_loss)
      games += 1

  w = 0

  for wl in range(len(outcome)):
      if outcome[wl] == "W":
          w += 1

  if w == 5 or w == 6:
      print("1")
  elif w == 3 or w == 4:
      print("2")
  elif w == 1 or w == 2:
      print("3")
  else:
      print("-1")

tournament_selection()      
