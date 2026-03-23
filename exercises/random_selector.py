
import random


def random_number():
    computer_choice = random.randint(1, 20)
    first_attempt = True
    while True:
        try:
            if first_attempt:
                user_choice = int(input("Select a number between 1 and 20: "))
                first_attempt = False
            elif computer_choice > user_choice:
                print("Try a higher number")
                user_choice = int(input("You guessed wrong try again: "))
            elif computer_choice < user_choice:
                print("Try a lower number")
                user_choice = int(input("You guessed wrong try again: "))
            elif user_choice == computer_choice:
                print("Great, you did it this time!!")
                break
        except ValueError:
            print("Words are not permitted, you must select a number")
            continue
            
            
random_number()