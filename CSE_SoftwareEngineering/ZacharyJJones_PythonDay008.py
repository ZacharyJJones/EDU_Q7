print("Your daily affirmations are available - You merely need to answer a few questions to receie your divine affirmations")
print()

name = input("Please tell me your name: ").lower()
day = input("What day of the week is it?: ").lower()
print()

if (name.min() == "z"):
  print("Great fortune awaits you on this", day, ", " + name)
elif (name.min() == "s" or name.min() == "p"):
  if (day == "monday" or day == "tuesday"):
    print("You are entering a powerful week,", name, ". Riches await if you are willing to take full advantage of incoming opportunities.")
  elif (day == "wednesday"):
    print("The middle of things is a trial and a respite both - through your duties completed, you will find those evasive answers.")
  elif (day == "thursday" or day == "friday"):
    print("Fight on. Fight on. Fight on. Your strength inspires and your persistence erodes the very walls which seek to contrain you. Find your peace and duty and walk boldly into life with each in hand.")
  else:
    print("Great success will find those who take care of themselves. Your aura glows and dazzles, yet you myst still hold yourself to higher standards,", name, ".")
else:
  print("Good things come to those your send their wills outward. Your efforts will pay off in ways greater than you can know, and your story shall be that of bliss.")