#globals
import datetime
import random
customers = {'customer1_id': 'customer1_pass', 'customer2_id': 'customer2_pass'}
managers = {'manager_id': 'manager_pass'}

products = {
    'RD001': {'name': 'Red Dress', 'unit_price': 5.0, 'stock': 100},
    'BS001': {'name': 'Blue Shoes', 'unit_price': 10.0, 'stock': 50},
    'BS002': {'name': 'Black Shirt', 'unit_price': 5.00, 'stock': 25},
}
orders = []
order_id_counter = 10001



# functions

def login():
    # Implement login functionality
    login_type = int(input('Choose 1 for manager, 0 for customer: '))
    if login_type == 1:
        user_id = input('Enter manager ID:')
        password = input('Enter manager password:')
        if user_id in managers and managers[user_id] == password:
            return 'manager', user_id
        else:
            print('Invalid manager ID or password.')
            return None, None
    elif login_type == 0:
        user_id = input('Enter your customer ID:')
        password = input('Enter your customer password:')
        if user_id in customers and customers[user_id] == password:
            return 'customer', user_id
        else:
            print('Invalid customer ID or password.')
            return None, None
    else:
        print('Invalid login type. Choose 1 for manager, or 0 for customer.')
        return None, None

#get date 
def get_date():
    start = datetime.date(2022,1,1)
    end = datetime.date(2023,12,31)
    order_date = start + (end - start) * random.random()

    return order_date 

def customer_menu(customer_id):
    global orders
    while True:
        print('Customer Menu:')
        choice = input('1. Submit Order\n2. View Order History\n3. Summary of orders\n4. Logout\n5. Exit\nChoose an option: ')
        if choice == '1':
            submit_order(customer_id)
        elif choice == '2':
            customer_view_orders(customer_id)
        elif choice =='3':
            customer_summary_orders()
        elif choice == '4':
            break
        elif choice =='5':
            exit()
        else:
            print("Invalid choice.")
            
def customer_summary_orders(): 
    pass
        
def manager_menu(manager_id):
    while True:
        print('Manager Menu:')
        choice = input('1. View All Orders\n2. Manager Order Summary\n3. Edit Prices\n4. Order More Inventory\n5. Logout\n6. Exit\n ')
        if choice == '1':
            manager_view_orders()
        elif choice == '2':
            manager_order_summary()
        elif choice == '3':
            edit_prices()
        elif choice == '4':
            inventory_reorder()
        elif choice == '5':
            manager_logout()
        elif choice =='6':
            exit()
        else:
            print("Invalid choice.")

def manager_view_orders():
    global orders
    print("Orders placed by all customers:")
    if orders:
        for order in orders:
            print_order(order)
    else:
        print('No orders found.')
        
def manager_order_summary():
    pass

def manager_logout(login_type):
    #says to wait until the end of the project. Will keep what I think will be the code
    if login_type == 1:
        logout_desire = input('Do you want to logout? (y/n)')
        if logout_desire.lower() == 'y':
            print('Manager logged out successfully. Goodbye!')
        elif logout_desire.lower() == 'n':
            pass
        else:
            print('Invalid input. Please enter "y" or "n".')
    else:
        pass


def edit_prices():
    global products
    
    print('Available Products and Current Prices:')
    for product_id, info in products.items():
        print(f"{product_id}: {info['name']} - ${info['unit_price']:.2f}")

    # Get the product ID to edit
    product_id = input("Enter the product ID you want to edit: ").strip().upper()

    # Check if the entered product ID exists
    if product_id in products:
        # Get the new unit price 
        new_price = float(input('Enter the new unit price: '))

        # Update product unit price
        products[product_id]['unit_price'] = new_price

        print(f'Price for Product ID {product_id} updated to ${new_price:.2f}')
    else:
        print(f'Product ID {product_id} not found')

def submit_order(customer_id):
    global order_id_counter
    print('Available Products:')
    for product_id, info in products.items():
        print(f"{product_id}: {info['name']} - ${info['unit_price']:.2f} - Stock: {info['stock']}")
    product_id = input("Enter the product ID you want to order: ")
    if product_id in products:
        quantity = int(input('Enter the quantity you want to order: '))
        if quantity <= products[product_id]['stock']:
            order_id = order_id_counter
            order_id_counter += 1
            order_date = get_date()
            order_price = quantity * products[product_id]['unit_price']
            product_name = products[product_id]['name']
            order = {
                'order_id': order_id,
                'order_date': order_date,
                'customer_id': customer_id,
                'product_id': product_id,
                'quantity': quantity,
                'order_price': order_price,
                'name': product_name,
                'date': order_date
            }
            orders.append(order)
            print('Order placed successfully!')
            update_stock(product_id, -quantity)  
            print_order(order)
        else:
            print('Not enough stock available for this product.')
    else:
        print('Invalid product ID.')

def update_stock(product_id, quantity):
    products[product_id]['stock'] -= quantity

def inventory_reorder():
    global products
    print("Current stock for all products:")
    for product_id, info in products.items():
        print(f'{product_id}: {info["name"]} - Stock: {info["stock"]}')

    reorder_option = input('Choose reorder quantity option: \n'
                           'a. Reorder set quantity of all products \n'
                           'b. Specify reorder amount for each individual product \n'
                           'c. Set a reorder quantitiy attribute for each product. \n'
                           'Choose an option (a/b/c): ').lower()
    if reorder_option == 'a':
        reorder_quantity = int(input('Enter the reorder quantity for all products: '))
        for product_id, info in products.items():
            info['stock'] += reorder_quantity
    elif reorder_option == 'b':
        for product_id, info in products.items():
            reorder_quantity = int(input(f'Enter the reorder quantity for product {product_id}: '))
            info['stock'] += reorder_quantity
            print(f'{info["name"]} replenished with {reorder_quantity} units.')
    elif reorder_option == 'c':
        for product_id, info in products.items():
            reorder_level = int(input(f'Enter reorder level for {info["name"]}: '))
            reorder_quantity = int(input(f'Enter reorder quantity for {info["name"]}: '))
            restock_amount = reorder_quantity - info['stock']
            info['reorder_level'] = reorder_level
            info['reorder_quantity'] = reorder_quantity
            print(f'Reorder attributes set for {info["name"]}: Reorder Level: {reorder_level}, Reorder Quantity: {reorder_quantity}')
            print(f'{info["name"]} replenished with {restock_amount} units')
            print('Reorder attributes updated successfully!')
    else:
        print('Invalid option. Please choose "a", "b", or "c".')


def print_order(order):
    print("Order Details:")
    print(f'Product Name: {order["name"]}')
    print(f"Order ID: {order['order_id']}")
    print(f"Product ID: {order['product_id']}")
    order_date = get_date()
    order_date_string = order_date.strftime("%m-%d-%Y")
    print(f'Order Date: {order_date_string:15s}')
    print(f"Quantity: {order['quantity']}")
    print(f"Total Price: ${order['order_price']:.2f}")

def customer_view_orders(customer_id):
    print('Orders placed by you:')
    orders_placed = [order for order in orders if order['customer_id'] == customer_id]
    if orders_placed:
        for order in orders_placed:
            print_order(order)
    
    else:
        print('No orders found for this customer.')

def reset():
    global orders
    orders.clear()  

#main
def main():
    global order_id_counter
    quit_program = False
    while not quit_program:
        print('Main Menu:')
        print('1. Login')
        print('2. Quit')
        choice = input('Choose an option: ')
        
        if choice == '1':
            user_type, user_id = login()
            if user_type == 'customer':
                customer_menu(user_id)
            elif user_type == 'manager':
                manager_menu(user_id)
            else:
                print('Invalid ID or password.')
        elif choice == '2':
            quit_program = True
        else:
            print('Invalid choice.')
main()
