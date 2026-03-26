orders_file = "orders.txt"

def order_drink():
    print("\n Choose one of the following drinks: ")
    print("1. Lemonade")
    print("2. Pepsi ")
    print("3. Natural Juice in Water/Milk")
    
    drink = input("Option: ")
    
    drinks = {
        "1": "Lemonade",
        "2": "Pepsi",
        "3": "Natural Juice in Water/Milk"
    }
    
    if drink in drinks:
        chosen_drink = drinks[drink]
        print(f"You've chosen {chosen_drink}. We're getting your order ready!!")
        
        with open("orders.txt", "a", encoding="utf-8") as file:
            file.write(chosen_drink + "\n")
    else:
        print("PLease try again")
    
def order_combo():
    print("\n Choose one of the following Combos: ")
    print("1. Colombian Combo")
    print("2. The Cheesy Burguer")
    print("3. SunnyDae")
    
    combo = input("Option: ")
    
    combos = {
        "1": "Colombian Combo",
        "2": "The Cheesy Burguer",
        "3": "SunnyDae"
        }
    
    if combo in combos:
        chosen_combo = combos[combo]
        print(f"You've chosen {chosen_combo}. We're getting your order ready!!")
        
        with open("orders.txt", "a", encoding="utf-8") as file:
            file.write(chosen_combo + "\n")
    else:
        print("PLease try again")