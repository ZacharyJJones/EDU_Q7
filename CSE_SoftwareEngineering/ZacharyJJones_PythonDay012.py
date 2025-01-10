print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?") # missing end quotation
ans1 = input("What language are we writing in?") # missing input function name
if ans1 == "python": # WORKS but inconsistent style for if statement no parentheses
  print("Correct")
else:
  print("Nope🙈") # missing end quote and end parentheses
ans2 = int(input("Which lesson number is this?")) # was not casting to int
if(ans2>12):
  print("We're not quite that far yet") # missing indentation
elif(ans2==12): # was incorrectly placed after the "else"
  print("That's right!")
else:
  print("We've gone well past that!")