print("== Super Duper Login System - Banking Made Awesome ==")
print()

username = input("Enter your username: ")
password = input("Enter your password: ")

if ((username == "username" or username == "admin") and (password == "password" or password == "admin" or password == "")):
   print("Welcome to the system! Please be responsible.")    
elif (username == "agatha12" and password == "m15s4gatha8"):
  print("Welcome to the system! Thank you for the cookies!")
elif (username == "abe_linky720" and password == "slinkyMcGrinky#2s*"):
  print("Welcome to the system! Please pay back your loans.")
else:
  print("Username or Password is incorrect. Please try again.")