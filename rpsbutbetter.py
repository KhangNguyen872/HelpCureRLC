import random

wanna_play = input("Wanna play rock, paper, scissors? y/n: ")


while wanna_play == "y":
    options = ['rock','paper','scissors']
    player_choice = input("Rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    
    print("Player:",str.capitalize(player_choice))
    print("Computer:",str.capitalize(computer_choice))

    if player_choice == computer_choice:
        print("You tied!")
    elif player_choice != computer_choice:
        if player_choice == options[0] and computer_choice == options[2] or player_choice == options[1] and computer_choice == options[0] or player_choice == options[2] and computer_choice == options[1]:
            print("You Win!")
            print(str.capitalize(player_choice),"beats",str.capitalize(computer_choice))
        elif player_choice == options[2] and computer_choice == options[0] or player_choice == options[0] and computer_choice == options[1] or player_choice == options[1] and computer_choice == options[2]:
            print("You Lose!")
            print(str.capitalize(computer_choice),"beats",str.capitalize(player_choice))
    wanna_play = input("Wanna play again? y/n: ")

if wanna_play == "n":
    print("Oh....I see how it is")