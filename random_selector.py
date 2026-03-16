
import random


def random_number():
    user_choice = int(input("Select a number between 1 and 20: "))
    computer_choice = random.randint(1, 20)
    if computer_choice == user_choice:
        print("Congratulations, you have guessed correctly")
        return  
    while True:
        if computer_choice > user_choice:
            print("Try a higher number")
            user_choice = int(input("You guessed wrong try again: "))
        elif computer_choice < user_choice:
            print("Try a lower number")
            user_choice = int(input("You guessed wrong try again: "))
        elif user_choice == computer_choice:
            print("Great, you did it this time!!")
            break
            
random_number() 
        
        



        
        
        