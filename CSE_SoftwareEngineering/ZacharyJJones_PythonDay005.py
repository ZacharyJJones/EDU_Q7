print("Which Character Are You? - Lorwyn 5 Edition")
print("Answer all questions with 'y' or 'n'!")
print()

ans1 = "y" == input("Are you a 'meowsive' lion-person with a penchant for lifegain?")
anyYes = ans1
if (ans1):
  print("Woohoo! You're Ajani Goldmane, famously known for cat people and betraying those cat people after turning into a half-alive robot terminator! Nice.")
else:
  print("Hmm... you're not Ajani Goldmane")
print()

if (not anyYes):
  ans2 = "y" == input("Does the concept of wiping peoples' minds and existing in the shadows of a dark and maniacal villain appeal to you?")
  anyYes = anyYes or ans2
  if (ans2):
    print("Woohoo! You're Jace Beleren, famously known for being a bad guy then a good guy then a bad guy again, then losing all your memories, then being a good guy one more time! And using all sorts of crazy mind manipulation magic along the way. Nice.")
  else:
    print("Hmm... you're not Jace Beleren")
  print()

if (not anyYes):
  ans3 = "y" == input("Are you a dark and ominous woman who magicks lost souls into zombified bodies?")
  anyYes = anyYes or ans3
  if (ans3):
    print("Woohoo! You're Liliana Vess, famously known for acting as a double agnet while Nicol Bolas nearly destroyed all of reality, and then securing the victory against that big dumb dragon with an unbelievable tidal wave of necrotic powers! Nice.")
  else:
    print("Hmm... you're not Liliana Vess")
  print()

if (not anyYes):
  ans4 = "y" == input("Do you like setting things on fire and running away from your problems (and discarding your hand)?")
  anyYes = anyYes or ans4
  if (ans4):
    print("Woohoo! You're Chandra Nalaar, famously known for setting things on fire, and for setting things on fire! Also known for reuniting with her estranged rebel mother and revolutionizing a society of tinkerers and metalsmiths! Nice.")
  else:
    print("Hmm... you're not Chandra Nalaar")
  print()
  
if (not anyYes):
  ans5 = "y" == input("Are you a big stinky man that likes cursed objects and wrestling bears?")
  anyYes = anyYes or ans5
  if (ans5):
    print("Woohoo! You're Garruk Wildspeaker, famously known for going crazy and murdering all sorts of important people, then disappearing for many years and living in a dark forest forever after. And also taming beasts.")
  else:
    print("Hmm, you're not Garruk Wildspeaker")
  print()

print()
if (anyYes):
  print("Looks like you found your answer!")
else:
  print("Hmm, that's weird! Looks like you aren't any of the original 5 Planeswalker characters from the totally Hip and Popular Collectible Card Game *NOT GAMLBING* Magic The Gathering which is so much fun to play! Wow!")