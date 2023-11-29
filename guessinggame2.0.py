import random

wanna_play = input("Wanna play a guessing game? y/n: ")

while wanna_play == "y":
    random_number = random.randint(1,10)
    player_guess = int(input("Guess a number between 1 and 10: "))

    if player_guess == random_number:
        print("Correct!")
        wanna_play = input("Wanna play again? y/n: ")
    elif player_guess != random_number:
        print("Wrong!")
        print("The correct answer was:",random_number)
        wanna_play = input("Wanna play again? y/n: ")

if wanna_play == "n":
    print("Oh....I see how it is")