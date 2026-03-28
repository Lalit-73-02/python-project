# Online Shopping Cart System

# Store items (Dictionary)
store = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 40,
    "eggs": 70
}

cart = set()  # unique items

def show_products():
    print("\n🛒 Available Products:")
    for item, price in store.items():
        print(f"{item} - ₹{price}")

def add_to_cart():
    item = input("Enter product to add: ").lower()
    
    if item in store:
        cart.add(item)  # set use
        print("✅ Item added to cart")
    else:
        print("❌ Product not available")

def remove_from_cart():
    item = input("Enter product to remove: ").lower()
    
    if item in cart:
        cart.remove(item)
        print("🗑️ Item removed")
    else:
        print("❌ Item not in cart")

def view_cart():
    print("\n🧺 Your Cart:")
    if len(cart) == 0:
        print("Cart is empty")
    else:
        total = 0
        for item in cart:
            price = store[item]
            print(f"{item} - ₹{price}")
            total += price
        
        print(f"\n💰 Total Bill = ₹{total}")

def menu():
    while True:
        print("\n===== SHOP MENU =====")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            show_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            view_cart()
        elif choice == '5':
            print("👋 Thank you for shopping!")
            break
        else:
            print("❌ Invalid choice")

# Run program
menu()