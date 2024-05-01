import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    print(f"The computer chose: {computer_choice}")

    if user_choice in choices:
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")

rock_paper_scissors()
