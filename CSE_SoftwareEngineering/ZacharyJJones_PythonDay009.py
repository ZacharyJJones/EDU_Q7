print("Birth Generation Identifier Tool 2000x+47")
print()

year = int(input("What year were you born?"))
gen = "unknown!!!"

if (year >= 1925 and year <= 1946): 
  gen = "The Traditionalists"
elif (year >= 1947 and year <= 1964):
  gen = "The Baby Boomers"
elif (1965 <= year and year <= 1981):
  gen = "Generation X"
elif (1982 <= year and year <= 1995):
  gen = "The Millenials"
elif (1996 <= year and year <= 2015):
  gen = "Generation X"

print("Your generation's name is...", gen)