import random

while True:
    user_action = input("Enter a choice: Rock, Paper, or Scissors: ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action} while the computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a Tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors. You Win!")
        else:
            print("Paper covers Rock. You Lose")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock. You Win!")
        else:
            print("Scissor cuts Paper. You Lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper. You Win!")
        else:
            print("Rock smashes Scissors. You Lose.")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break