print("=== Day 15 Loops ===")
print()

print("This program tells you what sound an animal makes!")
user_wants_to_exit = False

while (not user_wants_to_exit):
  print("What animal do you want to hear? ")
  user_input = input("Enter: ").lower()
  print()

  if (user_input == "cow"):
    print("moooooooooo")
  elif (user_input == "dog"):
    print("bark bark woof wooff aroof rorrf garf!!!!!")
  elif (user_input == "turtle"):
    print("... chomp ...")
  elif (user_input == "bird"):
    print("chirp tweet")
  else:
    print("uh oh! I don't know that animal!")

  user_wants_to_exit = input("Do you want to exit? yes/no?: ").lower() == "yes"
  pass

print()
print()
print("Thank you for using this program.")