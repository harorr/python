from menu import show_menu
from orders import order_combo, order_drink
from history import show_history

def main():
    while True:
        show_menu()
        option = input("Select an option: ")
        
        if option == "1":
            order_combo()
        elif option == "2":
            order_drink()
        elif option == "3":
            show_history()
        elif option == "4":
            print("\n Thanks for coming to McRolando's")
            break     
        else:
            print("Please select one of the given options")

if __name__ == "__main__":
    main()
