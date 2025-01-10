print("Rock. Paper. SCISSORS!!!!!! *exuberant cheering from the crowds*")
print("Best of 3. Anything that starts with R is rock, starts with P paper, S scissors!!!!!")
print()

def inputValid(s):
  return (s == "r" or s == "s" or s == "p")

def evaluateThrow(a, b):
  # handle all ties at same time
  if (a == b):
    return 0

  if (a == "r"):
    if (b == "s"):
      return 1
    else:
      return 2
  elif (a == "s"):
    if (b == "p"):
      return 1
    else:
      return 2
  else:
    if (b == "r"):
      return 1
    else:
      return 2
  pass

from getpass import getpass as input

p1 = 0
p2 = 0

while (p1 < 2 and p2 < 2):
  print("ANOTHER ROUND BEGINS!!!")
  print("The score is: ", p1, "(p1) to", p2, "(p2)")
  print()
  input1 = "_"
  while (not inputValid(input1)):
    input1 = (input("Player 1, make your move!!") + "_").lower()[0]
    if (not inputValid(input1)):
      print("invalid input!")

  input2 = "_"
  while (not inputValid(input2)):
    input2 = (input("Player 2, make your move!!") + "_").lower()[0]
    if (not inputValid(input2)):
      print("invalid input!")

  print()
  result = evaluateThrow(input1, input2)
  if (result == 1):
    print("Player 1 wins!")
    p1 += 1
  elif (result == 2):
    print("Player 2 wins!")
    p2 += 1
  else:
    print("That's a tie! Go again!!!!")
  print()
  print()

winner = "Player 1"
if (p2 > p1):
  winner = "Player 2"
print("The winner is decided... congratulations,", winner, "you have won!!!")