import random

'''
for x in range(0,5):
    print("your mom")

list1 = list(range(0,101))
print(list1)

for x in range(1,6):
    print('hello %s' % x)

for x in range(0,5):
    print(x + 1)

weight = 107
pounds = 2
for week in range(1,53):
    weight = weight + pounds
    print('Week %s = %s' % (week, weight))

'''

guess = input("Guess a number between 1 and 10: ")
guess = int(guess)
random_number = random.randint(1,10)

if guess == random_number:
    print("Correct! It was: ",random_number)
    repeat = input("Wanna play again? y/n: ")
elif guess != random_number:
    print("Wrong!")
    print("It was: ",random_number)
    repeat = input("Wanna play again? y/n: ")

while repeat == "y":
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    random_number = random.randint(1,10)
    if guess == random_number:
        print("Correct! It was: ",random_number)
        repeat = input("Wanna play again? y/n: ")
    elif guess != random_number:
        print("Wrong!")
        print("It was: ",random_number)
        repeat = input("Wanna play again? y/n: ")
    
if repeat == "n":
    print("Ok, Thanks for playing!")