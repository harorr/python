
def create_greeting(friend_name, favorite_drink):
    friend_name = friend_name.capitalize()
    favorite_drink = favorite_drink.capitalize()
    return (f"Hello {friend_name}, I hope you are having a wonderful day! Would you like a glass of {favorite_drink}?")
    
name_input = input()
drink_input = input()

print(create_greeting(name_input, drink_input))

