u3066193
 
Date: 17/09/2025

# Dictionary of items with prices and categories
menu_items = {
    "Coffee": {"price": 3.50, "category": "Beverage"},
    "Tea": {"price": 2.75, "category": "Beverage"},
    "Sandwich": {"price": 5.00, "category": "Food"},
    "Salad": {"price": 4.50, "category": "Food"},
    "Muffin": {"price": 2.25, "category": "Snack"},
    "Cookie": {"price": 1.75, "category": "Snack"}
}

# Cart as a list
cart = []

# Set for unique categories
categories = set()

# Function to display menu
def display_menu():
    print("\n--- Campus Café Menu ---")
    for item, details in menu_items.items():
        print(f"{item}: ${details['price']:.2f} ({details['category']})")
# Function to add item to cart
def add_to_cart(item_name):
    if item_name in menu_items:
        cart.append(item_name)
        categories.add(menu_items[item_name]["category"])
        print(f" Added {item_name} to cart.")
    else:
        print("coffee.")
# Function to print receipt
def print_receipt():
    print("\n--- Receipt ---")
    total = 0.0
    for item in cart:
        price = menu_items[item]["price"]
        print(f"{item}: ${price:.2f}")
        total += price
    print(f"\nTotal: ${total:.2f}")
    print(f"Unique categories in cart: {', '.join(categories)}")
    print("Thank you for visiting Campus Café!")

# Main loop
def checkout_console():
    running = True
    while running:
        display_menu()
        choice = input("\nEnter item to add to cart (or type 'done' to checkout): ").strip()
        if choice.lower() == "done":
            running = False
        else:
            add_to_cart(choice)

    print_receipt()

# Run the POS system
checkout_console()




Pseudocode
**********
# Define item prices using a dictionary
prices = {
    "coffee": 3.50,
    "tea": 2.75,
    "sandwich": 5.00,
    "salad": 4.25,
    "cookie": 1.50
}

# Define item categories using a dictionary
categories = {
    "coffee": "beverage",
    "tea": "beverage",
    "sandwich": "food",
    "salad": "food",
    "cookie": "dessert"
}
# Initialize cart as a list
cart = []

# Initialize unique categories as a set
unique_categories = set()

# Function to display menu
function display_menu():
    print("Welcome to Campus Café!")
    print("Menu:")
    for item in prices:
        print("- " + item + ": $" + format(prices[item], 2))

# Function to add item to cart
function add_to_cart(item):
    if item in prices:
        cart.append(item)
        unique_categories.add(categories[item])
        print(item + " added to cart.")
    else:
        print("Item not found.")

# Function to calculate total
function calculate_total():
    total = 0.0
    for item in cart:
        total = total + prices[item]
    return total

# Function to print receipt
function print_receipt():
    print("\n--- Receipt ---")
    for item in cart:
        print(item + " - $" + format(prices[item], 2))
    print("Total: $" + format(calculate_total(), 2))
    print("Categories in cart: " + join(unique_categories, ", "))
    print("Thank you for visiting Campus Café!")

# Main loop
running = true
while running:
    display_menu()
    print("Enter item to add to cart or type 'checkout' to finish:")
    user_input = input()

    if user_input == "checkout":
        running = false
    else:
        add_to_cart(user_input)

# After exiting loop, print receipt
print_receipt()
