
"""
Learning Python
Rock, Paper, Scissors
"""
"""
Este programa sera un juego de piedra, papel o tijera en que me pedira seleccionar una de las 3 opciones
y la comparara con la seleccion de la maquina, para finalmente determinar el ganador.
"""

import random

options = ["rock", "paper", "scissors"]

message = {
    "tie" : "We have a tie",
    "won" : "Yay you won",
    "lost" : "Damn you lost"
}

def decide_winner(user_choice, computer_choice):
    if user_choice not in options:
        print("You must select Rock, Paper or Scissors")
        return
    print (f"You selected {user_choice}")
    print(f"The machine selected {computer_choice}")
    if user_choice == computer_choice:
        print(message["tie"])
    elif (user_choice, computer_choice) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        print(message["won"])
    else: print(message["lost"])


def play_RPS():
    print("Rock, Paper, Scissors?")
    user_choice = input("Enter Rock, Paper or Scissors: ")
    user_choice = user_choice.lower()
    computer_choice = random.choice(options)
    decide_winner(user_choice, computer_choice)
    
    
number_rounds = int(input("How many rounds do you want to play?: "))
print(number_rounds)
for _ in range(number_rounds):
    play_RPS()

    
    
    
    
        
    
    
    
    

        





