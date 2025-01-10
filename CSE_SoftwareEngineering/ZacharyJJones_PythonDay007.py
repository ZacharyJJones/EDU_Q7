print("So You Think You Know Factorio Belts, Huh??")
print("--------------")
print("This state-of-the-art quiz will reveal the true extent of your knowledge regarding belts in the hit programmer-addicting game Factorio.")
print()
print()

knowledge_level = 0
print("Level 1:")
input1 = input("What is the name of the base-level belt that you start the game with?")
if (input1 == "Transport Belt" or input1 == "transport-belt"):
  print("> correct!")
  knowledge_level = knowledge_level + 1

  print()
  print()
  print("Level 2:")
  input2 = input("How many tiers of belts are there in the game as it is currently released?")
  if (input2 == "three" or input2 == "3"):
    knowledge_level = knowledge_level + 1
    print("> correct")
  else:
    print("> wrong")

  print()
  print()
  print("Level 3:")
  input3 = input("How many items per second will the max level transport belt in the upcoming 2.0 dlc launch 'Space Age' be able to transport, assuming all non-infinite research is completed?")
  if (input3 == "240"):
    knowledge_level = knowledge_level + 1
    print("> correct")
  else:
    print("> wrong")
else:
  print("Oh no, you couldn't even answer the first question properly! We in the industry call that an instant failure.")


print()
print()
if (knowledge_level == 0):
  print("OOF, yikes. Looks like you are terribly uneducated on this grand topic.")
elif (knowledge_level >= 1 and knowledge_level <= 2):
  print("Hey that is pretty good belt knowledge. It's clear you are still lacking somewhat, but you did a great job with this attempt!")
else:
  print("Wow! You are some kind of belt genius!")