orders_file = "orders.txt"

def show_history():
    try:
        print("\n Order History")
        with open(orders_file, "r", encoding="utf-8") as file:
            orders = file.readlines()
            if orders:
                for i, order in enumerate(orders, start=1):
                    print(str(i) + ". " + order.strip())
            else:
                print("There are no registered orders yet.")
    except FileNotFoundError:
        print("\n There isn't an order history")