name = input("What is your name? ")
print("Welcome to the Choose Your Own Adventure game, " + name + "!")

answer = input("You are in a dark forest. Do you want to go left or right? (L/R) ").lower()
if answer == "l":
    print("You encounter a wild beast!")
    answer = input("Do you want to fight or run? (F/R) ").lower()
    if answer == "f":
        print("You bravely fight the beast and win!")
    elif answer == "r":
        print("You run away safely.")
    else:
        print("Invalid choice. Game over.")
elif answer == "r":
    print("You find a treasure chest!")
    answer = input("Do you want to open it or leave it? (O/L) ").lower()
    if answer == "o":
        print("You found gold and jewels! You win!")
    elif answer == "l":
        print("You leave the treasure behind and walk away.")
    else:
        print("Invalid choice. Game over.")
else:
    print("Invalid choice. Game over.")

print("Thanks for playing, " + name + "!")
    