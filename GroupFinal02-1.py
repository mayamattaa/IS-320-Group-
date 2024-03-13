"""Stage2: Jessica Alonzo, Helen Mahari, Maya Matta, and Laina Delgado"""

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
            customer_logout()
            return  
        elif choice =='5':
            save_products("products.txt")
            save_orders("orders.txt")
            exit()
        else:
            print("Invalid choice.")


def customer_logout():
    print("Customer logged out successfully.")

def customer_summary_orders():
    global orders
    total_expense_per_product = {}
    
    for order in orders:
        product_id = order['product_id']
        order_price = order['order_price']
        
        if product_id in total_expense_per_product:
            total_expense_per_product[product_id] += order_price
        else:
            total_expense_per_product[product_id] = order_price
  
    print("Customer Summary Report")
    for product_id, total_expense in total_expense_per_product.items():
        print(f"Total expense per product {product_id}: {total_expense:.2f}")

customer_summary_orders()

        
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
            return
        elif choice =='6':
            save_products("products.txt")
            save_orders("orders.txt")
            exit()
        else:
            print("Invalid choice.")
            
def get_order_price(ord):
    return ord['order_price']

def get_product(ord):
    return ord['product_id']

#orders are sorted by order price (highest first) within each product. 
def manager_view_orders():
    global orders
    print("Orders placed by all customers:")
    line()
    print(f'|{"Product Name":^18s}|{"Order ID":^10s}|{"Product ID":^12s}|{"Order Date":^12s}|{"Quantity":^10s}|{"Total Price":^13s}|')
    line()
    
    orders_placed_price = sorted(orders, key=get_order_price, reverse=True)
    orders_placed = sorted(orders_placed_price, key=get_product)
    
    if orders_placed:
        for order in orders_placed:
             print(f'|{order["name"]:^18s}|{order["order_id"]:^10d}|{order["product_id"]:^12s}|{order["order_date"]:^12s}|{order["quantity"]:^10d}|${order["order_price"]:^12.2f}|')
             line()
    else:
        print('No orders found.')
        
def manager_order_summary():
    global orders, products
    
    total_revenue_per_product = {}
    total_orders_per_product = {}
    order_count_per_customer = {}
    high_value_orders = 0
    medium_value_orders = 0
    low_value_orders = 0
    
    high_cutoff = 100
    medium_cutoff = 10
  
    for order in orders:
        product_id = order['product_id']
        order_price = order['order_price']
        customer_id = order['customer_id']
    
        if product_id in total_revenue_per_product:
            total_revenue_per_product[product_id] += order_price
        else:
            total_revenue_per_product[product_id] = order_price
    
        if product_id in total_orders_per_product:
            total_orders_per_product[product_id] += 1
        else:
            total_orders_per_product[product_id] = 1
        
        if customer_id in order_count_per_customer:
            order_count_per_customer[customer_id] += 1
        else:
            order_count_per_customer[customer_id] = 1
        

        if order_price > high_cutoff:
            high_value_orders += order_price
        elif order_price < medium_cutoff:
            low_value_orders += order_price
        else:
            medium_value_orders += order_price
    
    total_revenue = sum(total_revenue_per_product.values())
    total_orders = sum(total_orders_per_product.values())
    average_revenue_per_order = total_revenue / total_orders if total_orders > 0 else 0
    
    print("Manager Summary Report")
    
    for product_id, total_revenue in total_revenue_per_product.items():
        average_revenue_per_order_per_product = total_revenue / total_orders_per_product[product_id] if total_orders_per_product[product_id] > 0 else 0
        print(f"Average revenue/order for product {product_id} is {average_revenue_per_order_per_product:.2f}")
    
    for product_id, total_revenue in total_revenue_per_product.items():
        print(f"Total revenue for product {product_id} is {total_revenue:.1f}")
   
    print(f"Average Revenue per Order: {average_revenue_per_order:.2f}")
    
    print("\nOrder Counts Per Customer")
    print("-----------------------")
    print("| Customer  |  Count  |")
    print("-----------------------")
    for customer_id, order_count in order_count_per_customer.items():
        print(f"|{customer_id:<10}|{order_count:^9}|")
    print("-----------------------")
    
    print(f"\nTotal Revenue for Low Value Orders (Below {medium_cutoff:.2f}):       {low_value_orders:.2f}")
    print(f"Total Revenue for High Value Orders (Above {high_cutoff:.2f}):      {high_value_orders:.2f}")
    print(f"Total Revenue for Medium Value Orders (The Rest):       {medium_value_orders:.2f}")

manager_order_summary()


def manager_logout():
    print("Manager logged out successfully.")

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
    global order_id_counter, orders, products
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
            order = {}

            order['order_id'] = order_id
            order['order_date'] = order_date.strftime("%m-%d-%Y")
            order['customer_id'] = customer_id
            order['product_id'] = product_id
            order['quantity'] = quantity
            order['order_price'] = order_price
            order['name'] = product_name   

            orders.append(order)
            print('Order placed successfully!')
            products[product_id]['stock'] -= quantity
            print_order(order)
        else:
            print('Not enough stock available for this product.')
    else:
        print('Invalid product ID.')
        
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
        
            if reorder_quantity > info['stock']:
                restock_amount = reorder_quantity - info['stock']
                info['reorder_level'] = reorder_level
                info['reorder_quantity'] = reorder_quantity
                info['stock'] += restock_amount  
                print(f'Reorder attributes set for {info["name"]}: Reorder Level: {reorder_level}, Reorder Quantity: {reorder_quantity}')
                print(f'{info["name"]} replenished with {restock_amount} units')
                print('Reorder attributes updated successfully!')
            else:
                print(f'No replenishment needed for {info["name"]}. Reorder quantity is not greater than current stock.')

def line():
    print('-' * 82)

def print_order(order):
    global orders
    
    print("Order Details:")
    line()
    print(f'|{"Product Name":^18s}|{"Order ID":^10s}|{"Product ID":^12s}|{"Order Date":^12s}|{"Quantity":^10s}|{"Total Price":^13s}|')
    line()
    
    print(f'|{order["name"]:^18s}|{order["order_id"]:^10d}|{order["product_id"]:^12s}|{order["order_date"]:^12s}|{order["quantity"]:^10d}|${order["order_price"]:^12.2f}|')
    line()

def get_order_date(ords_plc):
    return datetime.datetime.strptime(ords_plc['order_date'], ("%m-%d-%Y"))

def customer_view_orders(customer_id):
    global orders
    print('Orders placed by you:')
    print("Order Details:")
    line()
    print(f'|{"Product Name":^18s}|{"Order ID":^10s}|{"Product ID":^12s}|{"Order Date":^12s}|{"Quantity":^10s}|{"Total Price":^13s}|')
    line()
    orders_placed = [order for order in orders if order['customer_id'] == customer_id]
    orders_placed = sorted(orders_placed, key=get_order_date, reverse=False)

    if orders_placed:
            for order in orders_placed:
                if customer_id == order['customer_id']:
                    
                    print(f'|{order["name"]:^18s}|{order["order_id"]:^10d}|{order["product_id"]:^12s}|{order["order_date"]:^12s}|{order["quantity"]:^10d}|${order["order_price"]:^12.2f}|')
                    line()
    else:
        print('No orders found for this customer.')

def save_products(filename):
    with open(filename, 'w') as file:
        for product_id, info in products.items():
           file.write(f"{product_id},{info['name']},{info['unit_price']},{info['stock']}\n")


def load_products(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                product_id, name, unit_price, stock = line.strip().split(',')
                products[product_id] = {'name': name, 'unit_price': float(unit_price), 'stock': int(stock)}
    except FileNotFoundError:
        print("No product file found. Using default products.")


def save_orders(filename):
    with open(filename, 'w') as file:
        for order in orders:
            file.write(f"{order['order_id']},{order['order_date']},{order['customer_id']},{order['product_id']},{order['quantity']},{order['order_price']}\n")


def load_orders():
    filename='loadFinal.txt'
    print("IN LOAD ORDERS")
    try:
        with open(filename, 'r') as file:
            print("OPENED FILE")
            lines = file.readlines()
            for l in lines:
                print(l)
                name, customer_id, order_id, product_id, order_date, quantity, order_price = l.strip().split(',')
                orders.append({'name': name, 'customer_id': customer_id, 'order_id': order_id, 'product_id': product_id, 'order_date': order_date, 'quantity': int(quantity), 'order_price': float(order_price)})
    except FileNotFoundError:
        print("No order file found. No orders to load.")

def reset():
    global orders
    orders.clear()  

"""def save_products(filename):
    with open(filename, 'w') as file:
        for product_id, info in products.items():
            file.write(f"{product_id},{Name ['name']},{info['unit_price']},{info['stock']}\n")


#def load_products(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                product_id, name, unit_price, stock = line.strip().split(',')
                products[product_id] = {'name': name, 'unit_price': float(unit_price), 'stock': int(stock)}
    except FileNotFoundError:
        print("No product file found. Using default products.")


def save_orders(filename):
    with open(filename, 'w') as file:
        for order in orders:
            file.write(f"{order['order_id']},{order['order_date']},{order['customer_id']},{order['product_id']},{order['quantity']},{order['order_price']}\n")
"""


#main
def main():
    global order_id_counter
    load_orders()
    quit_program = False
    while not quit_program:
        print('Main Menu:')
        print('1. Login')
        print('2. Quit')
        
        try:
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
                save_products("products.txt")
                save_orders("orders.txt")
                quit_program = True
            else:
                print('Invalid choice.')
        except ValueError:
            print('Invalid input. Please enter a number.')

if __name__ == '__main__':
    main()