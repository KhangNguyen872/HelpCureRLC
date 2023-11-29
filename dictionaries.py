import random

state_capitals = {"Alabama" : "Montgomery",
                  "Alaska" : "Juneau",
                  "Arizona" : "Phoenix",
                  "Arkansas" : "Little Rock",
                  "California" : "Sacramento",
                  "Colorado" : "Denver",
                  "Connecticut" : "Hartford",
                  "Delaware" : "Dover",
                  "Florida" : "Tallahassee",
                  "Georgia" : "Atlanta",
                  "Hawaii" : "Honolulu",
                  "Idaho" : "Boise",
                  "Illinois" : "Springfield",
                  "Indiana" : "Indianapolis",
                  "Iowa" : "Des Moine",
                  "Kansas" : "Topeka",
                  "Kentucky" : "Frankfort",
                  "Louisiana" : "Baton Rouge",
                  "Maine" : "Augusta",
                  "Maryland" : "Annapolis",
                  "Massachusetts" : "Boston",
                  "Michigan" : "Lansing",
                  "Minnesota" : "Minneapolis",
                  "Mississippi" : "Jackson",
                  "Missouri" : "Jefferson City",
                  "Montana" : "Helena",
                  "Nebraska" : "Lincoln",
                  "Nevada" : "Carson City",
                  "New Hampshire" : "Concord",
                  "New Jersey" : "Trenton",
                  "New Mexico" : "Santa Fe",
                  "New York" : "New York City",
                  "North Carolina" : "Raleigh",
                  "North Dakota" : "Bismarck",
                  "Ohio" : "Columbus",
                  "Oklahoma" : "Oklahoma City",
                  "Oregon" : "Salem",
                  "Pennsylvania" : "Pittsburgh",
                  "Rhode Island" : "Providence",
                  "South Carolina" : "Columbia",
                  "South Dakota" : "Pierre",
                  "Tennessee" : "Nashville",
                  "Texas" : "Austin",
                  "Utah" : "Salt Lake City",
                  "Vermont" : "Montpelier",
                  "Virginia" : "Richmond",
                  "Washington" : "Olympia",
                  "West Virginia" : "Charleston",
                  "Wisconsin" : "Madison",
                  "Wyoming" : "Cheyenne"}

# User_Query = input("What state capital would you like to know?: ")
# print("The capital of ",User_Query,"is", state_capitals[User_Query])

print("Lets play a game of guess the capital!")

question = random.choice(list(state_capitals))
query = print("Guess the capital of: ", question)
player_answer = input("Your answer: ")
player_answer = str.capitalize(player_answer)
real_answer = state_capitals[question]

if player_answer == real_answer:
    print("Thats correct!")
else:
    print("Thats wrong!")
    print("It was:", real_answer)

play_again = input("Do you want to play again? y/n: ")

while play_again == "y":
    question = random.choice(list(state_capitals))
    query = print("Guess the capital of: ", question)
    player_answer = input("Your answer: ")
    player_answer = str.capitalize(player_answer)
    real_answer = state_capitals[question]

    if player_answer == real_answer:
        print("Thats correct!")
    else:
        print("Thats wrong!")
        print("It was:", real_answer)

    play_again = input("Do you want to play again? y/n: ")

if play_again == "n":
    print("Thanks for playing!")