print("python day 25 - health")
import random
print()
print()

def rollDie(sides):
  return random.randint(1, sides)


# I decided to break from the mold a bit and make health based on name length
def getCharHealth(name):
  hp = 0
  for i in range(len(name)):
    hp += rollDie(len(name))
  return hp


rolling = True
while (rolling):
  name = input("Name your character: ")
  print(name, "has", getCharHealth(name), "health.")

  print()
  again = input("Make another character?: ")
  rolling = again == "yes"
  pass