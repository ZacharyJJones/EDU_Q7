print("python day 21 - math facts 2")
print("Times Tables POP QUIZ Bring Your Own Bnumber")
print()


start = int(input("What number should the times table be for?: "))
print()

print("Now, for each equation shown, fill in the answer!")
print()

score = 0
maxMult = 10
# we will start at two because there is no point asking what 1 * X is.
for i in range(2, maxMult + 1):
  print()
  print(start, "x", i)
  answer = start * i
  guess = int(input("The answer is?: "))
  if (answer == guess):
    print("correct!")
    score += 1
  else:
    print("wrong!")


print()
print()
print("All done! You scored", score, "out of", (maxMult-1), "points.")