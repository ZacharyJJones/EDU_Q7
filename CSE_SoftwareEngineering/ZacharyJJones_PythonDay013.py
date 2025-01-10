testName = input("What was the name of this test?: ")
testScore = int(input("How many points did you score?: "))
testMax = int(input("... And how many points were possible to score?: "))
print()
print()
print("Calculating...")
print()
print()
print("...")

scorePercent = testScore * 100 / testMax

letterGrade = "?"
if (scorePercent >= 90):
  letterGrade = "SS+"
elif (scorePercent >= 80):
  letterGrade = "S"
elif (scorePercent >= 70):
  letterGrade = "A"
elif (scorePercent >= 60):
  letterGrade = "B"
elif (scorePercent >= 50):
  letterGrade = "C"
elif (scorePercent >= 40):
  letterGrade = "D"
elif (scorePercent >= 30):
  letterGrade = "D-"
elif (scorePercent >= 20):
  letterGrade = "E"
elif (scorePercent >= 10):
  letterGrade = "E-"
else:
  letterGrade = "F"

print("Your grade on the", testName, "test was", letterGrade, "(", scorePercent, "%)")

