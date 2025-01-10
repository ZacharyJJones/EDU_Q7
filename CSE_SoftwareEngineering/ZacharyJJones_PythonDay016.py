print("== Day 16 ==")
print("Fill in the blank lyrics!!")

guesses_made = 0
while (True):
  guesses_made = guesses_made + 1
  print()
  print("Somebody once told me, the _____ is gonna roll me //")
  print()
  lyric = input("Guess the missing word in the lyric!: ").lower()

  if (lyric == "world"):
    print("Correct!!")
    break
  else:
    print("Wrong! try again!")
  print()

print("Congrats! It took you " + str(guesses_made) + " tries!")

