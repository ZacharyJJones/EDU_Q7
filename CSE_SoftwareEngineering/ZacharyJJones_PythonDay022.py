import random
print("python 22 - libraries")
print("Guess A Number Game! BUT RANDOM NOW")


numberToGuess = random.randInt(1, 1000000)
playerWon = False
playerGuessCount = 0
playerGuessLow = 0
playerGuessHigh = 1000000
while (not playerWon):
  print("The number is somewhere between", playerGuessLow, "and", playerGuessHigh)
  print()

  guess = int(input("Enter your guess: "))
  playerGuessCount += 1
  if (guess < 0):
    break

  if (guess == numberToGuess):
    playerWon = True
    break
  elif (numberToGuess < guess):
    print("Too high! Try again.")
    playerGuessHigh = min(playerGuessHigh, guess)
  else:
    print("Too low! Try again.")
    playerGuessLow = max(playerGuessLow, guess)
  pass


if (playerWon):
  print("Congrats, you guessed the number!")
  print("... and it only took you", playerGuessCount, "guesses!")
  pass
else:
  print()
  print("Hey, that's not how you play the game! Now you have to start over.")