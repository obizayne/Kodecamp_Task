# Task 4: Shopping Cart System

# Scenario: Simulate a mini-store system.

# Instructions:

# - Show a list of available items with prices (use a dictionary)

# - Let the user "add to cart" by entering item name and quantity

# - Store cart in a list of dictionaries:

#  {"item": "Rice", "quantity": 2, "price": 400}

# - Calculate total bill

# - Option to remove an item or clear cart

# - Loop until user exits

# - Handle invalid inputs and missing items

cart = [{"item": "Rice", "quantity": 2, "price": 400},
        {"item": "Beans", "quantity": 1, "price": 200}, 
        {"item": "Sugar", "quantity": 3, "price": 150}] 

def bill():
    total = 0
    for item in cart:
        total += item["quantity"] * item["price"]
    return total

def remove_item():
    item_name = input("Please input the item name to remove: ")
    for item in cart:
        if item["item"].lower() == item_name.lower():
            cart.remove(item)
            print(f"{item_name} has been removed from the cart.")
            return
    print(f"{item_name} not found in the cart.")
def clear_cart():
    cart.clear()
    print("Cart has been cleared.")
    
def add_to_cart():
    item_name = input("Please input the item name to add: ")
    if not item_name:
        print("Item name cannot be empty.")
        return
    for item in cart:
        if item["item"].lower() == item_name.lower():
            item["quantity"] += quantity
            print(f"{quantity} {item_name}(s) added to the cart.")
            return
    quantity = int(input("Please input the quantity: "))
    price = float(input(f"Please input the price for {item_name}: "))
    new_item = {"item": item_name, "quantity": quantity, "price": price}
    cart.append(new_item)
    print(f"{item_name} has been added to the cart.")
    
def menu():
    print("Options:")
    print("1. Add to Cart")
    print("2. Remove Item")
    print("3. Clear Cart")
    print("4. View Cart")
    print("5. Calculate Total Bill")
    print("6. Exit")
    print("Please select an option (1-6):")
    
def app():
    while True:
        menu()
        try:
            choice = int(input())
            if choice == 1:
                add_to_cart()
            elif choice == 2:
                remove_item()
            elif choice == 3:
                accept = input("Are you sure you want to clear the cart? (yes/no): ")
                if accept.lower() == 'yes':
                    clear_cart()
                else:
                    print("Cart not cleared.")
                    return
            elif choice == 4:
                print("Current Cart:")
                for item in cart:
                    print(f"{item['item']} - Quantity: {item['quantity']}, Price: {item['price']}")
            elif choice == 5:
                total = bill()
                print(f"Total Bill: {total}")
            elif choice == 6:
                print("Exiting the shopping cart system.")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError as e:
            print("Invalid input. Please enter a number between 1 and 6.")
app()