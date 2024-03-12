import json

products = []
orders = []

def make_products():
    # Code to initialize products (if needed)
    #sample product list
    products.append({"id": 1, "name": "Product A", "price": 20.0, "in_stock": True})
    products.append({"id": 2, "name": "Product B", "price": 30.0, "in_stock": False})
    products.append({"id": 3, "name": "Product C", "price": 25.0, "in_stock": True})


def save(filename='products.json'):
    global products, orders
    with open(filename, 'w') as file:
        #save products:
        json.dump({"products": products, "orders": orders}, file, indent=2)
        #save orders:
        file.write('\n')
        for order in orders:
            order_date = order['order_date'].strftime('%m-%d-%Y')
            file.write(json.dumps(order) + '\n')
    print(f"Products saved to {filename}")

# def save(filename='products.json'):
#     global products, orders
#     data = {"products": products, "orders": orders}
#     with open(filename, 'w') as file:
#         json.dump(data, file, indent=2)
#     print(f"Products and orders saved to {filename}")

 
def load(filename='products.json'):
    global products, orders
    make_products()
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            products = data.get('products', [])
            orders = data.get('orders', [])
            order_id_counter = data.get('order_id_counter', 10001)  # Default start value if not found
            print(f"Products and orders loaded from {filename}")
            # data = json.load(file)
            # global products
            # products = data
            # print(f"Products loaded from {filename}")
            
    except FileNotFoundError:
        print(f"File {filename} not found. Loading default products.")
        # Fill the global products with default data if file not found
        # make_products()

if __name__ == '__main__':
    make_products()
    save()


# def main():
#     quit_program = False
#     while not quit_program:
#         print('1. Submit 2. Load 3. Summary 4. Save 5. Display 6. Search 7. Reset 8. Exit')
#         choice = int(input('Enter choice: '))
#         if choice == 1:
#             submit()
#         elif choice == 2:
#             load()
#         elif choice == 3:
#             summary()
#         elif choice == 4:
#             save()
#         elif choice == 5:
#             display()
#         elif choice == 6:
#             search()
#         elif choice == 7:
#             reset()
#         elif choice == 8:
#             quit_program = True

#     if __name__ == "__main__":
#         main()
