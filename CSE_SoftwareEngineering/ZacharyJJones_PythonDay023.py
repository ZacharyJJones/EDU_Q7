print("python day 23 - they are called functions.")

def checkLoginDetails(username, password):
  return (username == "Johann Cenari") and (password == "********")

loggedIn = False
while (not loggedIn):
  print()
  print("Please enter your login details.")
  username = input("Username: ")
  password = input("Password: ")
  loggedIn = checkLoginDetails(username, password)
  if (not loggedIn):
    print("well... that's just not right. Try again?")
    
print()
print("You are logged in!")