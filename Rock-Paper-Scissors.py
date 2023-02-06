import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you choose {player}, computer choose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers Rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            return "Scissor cuts Paper! You lose."
        else:
            return "Paper covers Rock! You win!"
    elif player == "scissor":
        if computer == "paper":
            return "Scissor cuts Paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

num_matches = int(input("Enter the number of matches you want to play: "))
for i in range(num_matches):
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    
