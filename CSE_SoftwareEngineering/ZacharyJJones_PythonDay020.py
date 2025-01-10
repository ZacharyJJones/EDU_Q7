print("Day 20 - Range continued")
print()

start = int(input("What number to start at?: "))
end = int(input("What number to end before reaching?: "))
increment = int(input("What number to increment by?: "))

for i in range(start, end, increment):
  print(i)