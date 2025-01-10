totalBill = float(input("What was the bill?: "))
numPeople = int(input("How many people is the bill being split between?: "))
tipPercent = float(input("What is the tip in % form? (e.g. 25 is 25%): "))

billWithTip = totalBill * (1 + tipPercent/100)

myBill = billWithTip / numPeople

print()
print("Each person owes", myBill, "dollars!")