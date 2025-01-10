print("Python day 24 - infinite size dice")

import random

print()
print()

def rollDie(sides):
  print("You rolled", random.randint(1, sides))


rolling = True
while (rolling):
  sides = int(input("How many sides on this die?: "))
  rollDie(sides)

  print()
  again = input("Roll again?")
  rolling = again == "yes"
  pass

# The genius of this program is that it (rightly) assumes that the user wants to stop using it as soon as possible, so it provides the most possible ways to NOT continue rolling dice.