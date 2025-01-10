# Gwanju Chung
# Jaskaran Sahota
# Zachary Jones


# Gets the sum of prices before discounts are applied
def calculateTotal(items):
  total = 0
  for i in items:
    total += i[1] * i[2]
  return total

# Apply a discount to the amount if it is over a certain value
def applyDiscount(amount):
  if amount > 100:
    return amount * 0.9
  return amount

# Get total cost of items and display as a receipt
def processReceipt(items):
  total = calculateTotal(items)
  total = applyDiscount(total)

  printReceipt(total, items)

def printReceipt(total, items):
  print("----- Receipt -----")
  for i in items:
    printReceiptItem(i)
  print("-------------------")
  print(f"Total: ${total}")
  print("-------------------")

def printReceiptItem(item):
    print(f"{item[0]}: {item[1]} x ${item[2]}")


# Collection of items that a user is purchasing
groceryCart = [["Apple", 5, 2], ["Banana", 3, 1], ["Orange", 4, 1.5]]

processReceipt(groceryCart)
