"""
manager_view_orders():  the only difference with customer view 
is that the manager 
gets to see all the orders by all the customers. 
So this will be the same as your initial display_orders() 
before implementing login.  
Dependency: same as customer view orders.
manager_order_summary():  can leave blank. 
 Our aim is to generate totals, counts, 
 remaining stock per product,  and to find customers 
 who ordered more than once. may add more details.  
 Dependent on: order representation. 
 Can be done independently. R
 ecommended that someone comfortable with lists and 
 dictionaries take charge of this function as it 
 offers more scope for adding more analytics on your own.

edit_prices() :   allows the manager to choose a product, specify a new unit_price for it which will then update universally.     Can be done independently. Depends on: how product prices are represented.

"""# Sample data structures to represent orders and product prices
# Sample data structures to represent orders and product prices
# Sample data structures to represent orders and product prices
orders = []  # cooming from other code?? 
products = {}  # comiong from other code?? 

# functions
def manager_view_orders():
    global orders
    if not orders:
        print("No orders found.")
    else:
        print("All Orders from All Customers:")
        for order in orders:
            print(f"Order ID: {order['order_id']}, Customer ID: {order['customer_id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}")

def manager_order_summary():
    # Leave the implementation blank for now
    pass

def edit_prices():
    global products

    # Display available products and their current prices
    print("Available Products and Current Prices:")
    for product_id, info in products.items():
        print(f"{product_id}: {info['name']} - ${info['unit_price']:.2f}")

    # Get the product ID to edit
    product_id = input("Enter the product ID you want to edit: ").strip().upper()

    # Check if the entered product ID exists
    if product_id in products:
        # Get the new unit price 
        new_price = float(input("Enter the new unit price: "))

        # Update product unit price
        products[product_id]['unit_price'] = new_price

        print(f"Price for Product ID {product_id} updated to ${new_price:.2f}")
    else:
        print(f"Product ID {product_id} not found")


# Manager menu function
def manager_menu(manager_id):
    while True:
        print("Manager Menu:")
        choice = input("1. View All Orders 2. Manager Order Summary 3. Edit Prices\n4. Order More Inventory, 5. Logout: ")
        if choice == '1':
            manager_view_orders()
        elif choice == '2':
            manager_order_summary()
        elif choice == '3':
            edit_prices()
        elif choice == '4':
            # Implement order more inventory functionality
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# Main program
def main():
    manager_id = "your_manager_id"  # Replace with actual manager ID
    manager_menu(manager_id)

# Call the main program
if __name__ == "__main__":
    main()





