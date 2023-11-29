import random

def win_function():
    if player_choice == "rock" and computer_choice == "Scissors":
        print("Congrats! You Win!")
    if player_choice == "paper" and computer_choice == "Rock":
        print("Congrats! You Win!")
    if player_choice == "scissors" and computer_choice == "Paper":
        print("Congrats! You Win!")

def tie_function():
    if player_choice == "rock" and computer_choice == "Rock":
        print("You Tied!")
    if player_choice == "paper" and computer_choice == "Paper":
        print("You Tied!")
    if player_choice == "scissors" and computer_choice == "Scissors":
        print("You Tied!")

def lose_function():
    if player_choice == "rock" and computer_choice == "Paper":
        print("You lost!")
    if player_choice == "paper" and computer_choice == "Scissors":
        print("You lost!")
    if player_choice == "scissors" and computer_choice == "Rock":
        print("You lost!")

player_choice = input("Choose rock, paper, or scissors (spelled correctly, no capitals): ")
player_choice = player_choice.lower()
computer_choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(computer_choice)
choices = {"Player": player_choice, "Computer": computer_choice}
print("Player: ", choices["Player"])
print("Computer: ", choices["Computer"])
win_function()
tie_function()
lose_function()

play_again = input("Do you want to play again? y/n: ")

while play_again == "y":
    player_choice = input("Choose rock, paper, or scissors: ")
    player_choice = player_choice.lower()
    computer_choice = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choice)
    choices = {"Player": player_choice, "Computer": computer_choice}
    print("Player: ", choices["Player"])
    print("Computer: ", choices["Computer"])
    win_function()
    tie_function()
    lose_function()
    play_again = input("Do you want to play again? y/n: ")

if play_again == "n":
    print("Thanks for playing!")