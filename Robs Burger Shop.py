# Robs Mcdonalds

print("Welcome to King Robs Burgers!")

# Ask for the customer's name
name = input("May I have your name, please? ")
print("Thank you, " + name + "!")

# Show the customer the menu
print("What can I get for you? Our menu options include: Big Macs, Quarter Pounders, or Fries.")

# Ask for the customer's order and calculate the total
order = input("What would you like to order? ")
total = 0
items = []
while order.lower() != "done":
    if order.lower() in ["big mac", "bigmac", "big mack", "bigmack", "bm"]:
        total += 4.99
        items.append("Big Mac")
    elif order.lower() in ["quarter pounder", "quarterpounder", "quarter", "qp"]:
        total += 5.99
        items.append("Quarter Pounder")
    elif order.lower() in ["fries", "fry", "f", "fr"]:
        total += 2.49
        items.append("Fries")
    else:
        print("I'm sorry, " + order + " is not a valid option.")
    order = input("Anything else? (Enter 'Done' when finished) ")

# Confirm the order and name, and show the total
if len(items) == 0:
    print("Sorry, it seems you didn't order anything.")
else:
    print("Thank you for your order, " + name + "! You ordered:")
    for item in items:
        print("- " + item)
    print("Your total comes to $" + str(total) + ". Please pull up to the first window to pay.")
