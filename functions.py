import random


# Function to show title
def welcome():
    print("=== Rock Paper Scissors ===")


# Function for player
def player_choice():
    return input("Enter Rock, Paper or Scissors: ").capitalize()


# Function for computer
def computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


# Function to check winner
def winner(player, computer):

    print("\nYou Chose:", player)
    print("Computer Chose:", computer)

    if player == computer:
        print("It's a Tie!")

    elif player == "Rock":
        if computer == "Scissors":
            print("You Win!")
        else:
            print("Computer Wins!")

    elif player == "Paper":
        if computer == "Rock":
            print("You Win!")
        else:
            print("Computer Wins!")

    elif player == "Scissors":
        if computer == "Paper":
            print("You Win!")
        else:
            print("Computer Wins!")

    else:
        print("Invalid Choice!")


# Main Program
welcome()

player = player_choice()

computer = computer_choice()

winner(player, computer)
