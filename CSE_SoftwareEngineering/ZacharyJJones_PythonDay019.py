print("python day 19 for loop")
print()

print("Loan Calculator for 5% APR on $1000 initial amount. 10 year duration.")
# kind of lacking in the user input department, isnt it?

loan = 1000.00
for i in range(10):
  loan *= 1.05
  pass

print()
print("You owe $", loan)
print("... yikes")