menu = {
    "Pasta": 120,
    "Burger": 80,
    "Pizza": 200,
    "Sandwich": 60,
}

print("Welcome to Aditya's Cafe!!")
print("'Pasta': 120\n'Burger': 80\n'Pizza': 200\n'Sandwich': 60")

order_total = 0

item_1 = input("Please enter your first order: ")

if item_1 in menu:
    order_total = order_total + menu[item_1]
    print("Your order has been added!!")
else:
    print("Sorry! Order something else.")

another_order = input("Do you want to add something more? (Yes/No): ")

if another_order.lower() == "yes":
    item_2 = input("Enter your second order: ")
    if item_2 in menu:
        order_total = menu[item_1] + menu[item_2]
        print("Your order has been added!!")
    else:
        print("Sorry! Order something else.")

print(f"Total bill is: {order_total}")
print("Thanks!! Visit again 😊")
