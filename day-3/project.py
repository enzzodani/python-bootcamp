
print("Welcome to Prision. Your mission is to escape the prision.") 

print("You are in a prision. But they left open two doors, the left door and the right door.\nWhat door do you want to pick? ")
choice_one = input().lower()

if choice_one == "right":
    print("You open a door to the guards room. Game over.")
else:
    print("You open a door to a boat's room.")
    choice_two = input("Do you want to take a boat or swin? Boat or Swin? ").lower()

    if choice_two == "swin":
        print("You drowned. Game over.")
    else:
        print("You arive in an island with 3 paths. The tree path, the river path and the mountain path. ")
        choice_three = input("Tree, River or Mountain? ").lower()

        if choice_three == "tree":
            print("You've lost. Game over")
        elif choice_three == "mountain":
            print("You've fall. Game over")
        else:
            print("Congratulations. You beat the game.")
