
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0


def get_winner(user, computer):

    if user == computer:
        return "draw"

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "user"

    else:
        return "computer"


def play_game():
    global user_score, computer_score, draws

    print("\n====== ROCK PAPER SCISSORS ======")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    while True:
        user_choice = input("\nEnter your choice: ").strip().lower()

        if user_choice == "exit" or user_choice == "4":
            break

        if user_choice in ["1", "rock"]:
            user_choice = "rock"
        elif user_choice in ["2", "paper"]:
            user_choice = "paper"
        elif user_choice in ["3", "scissors"]:
            user_choice = "scissors"
        else:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou selected: {user_choice}")
        print(f"Computer selected: {computer_choice}")

        result = get_winner(user_choice, computer_choice)

        if result == "user":
            print("Congratulations! You win this round!")
            user_score += 1

        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("It's a draw!")
            draws += 1

        print("\n====== SCOREBOARD ======")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print(f"Draws: {draws}")

    print("\n====== FINAL RESULT ======")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    print(f"Draws: {draws}")

    if user_score > computer_score:
        print("You are the overall winner! 🏆")
    elif computer_score > user_score:
        print("Computer is the overall winner!")
    else:
        print("The game ended in a tie!")


play_game()
