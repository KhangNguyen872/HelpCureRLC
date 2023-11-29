import random

def check_function():
    if player_choice == computer_choice:
        print("You tied!")
    elif player_choice != computer_choice:
        if player_choice == options[0] and computer_choice == options[2] or player_choice == options[1] and computer_choice == options[0] or player_choice == options[2] and computer_choice == options[1]:
            print("You Win!")
            print(str.capitalize(player_choice),"beats",str.capitalize(computer_choice))
        elif player_choice == options[2] and computer_choice == options[0] or player_choice == options[0] and computer_choice == options[1] or player_choice == options[1] and computer_choice == options[2]:
            print("You Lose!")
            print(str.capitalize(computer_choice),"beats",str.capitalize(player_choice))

options = ['rock','paper','scissors']
wanna_play = input("Wanna play rock, paper, scissors? y/n: ")

while wanna_play == "y":
    player_choice = input("Rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print("Player: " + player_choice + "\nComputer: " + computer_choice)
    print(check_function())
    wanna_play = ("Wanna play again? y/n: ")