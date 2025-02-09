import random
import rock_module

choices = ["rock", "paper", "scissors"]
modules = [rock_module.Rock, rock_module.Paper, rock_module.Scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

print(f"Your choice is {choices[user_choice]}\n {modules[user_choice]}")
    
computer_choice = random.randint(0,2)

print(f"Computer choice is {choices[computer_choice]}\n {modules[computer_choice]}")


if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You won")
elif user_choice == 1:
    if computer_choice == 0:
        print("You won")
    else:
        print("You lose")
elif user_choice == 2: 
    if computer_choice == 0:
        print("You lose")
    else:
        print("You won")
