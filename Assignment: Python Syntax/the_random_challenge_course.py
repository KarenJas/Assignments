'''8. The Random Challenge Course'''
    #Task 1: The Guessing Game
import random

game_number = random.randint(1,5)
input_guess = int(input("Guess a number: "))
if game_number == input_guess:
    print("You are correct!")
elif input_guess < game_number:
    int(input("guess higher: "))
    if game_number == input_guess:
        print("You are correct!")
    else:
        print("better luck next time!")
elif input_guess > game_number:
    int(input("Guess lower: "))
    if game_number == input_guess:
        print("You are correct!")
    else:
        print("better luck next time!")

    #Task 2: The Magic 8-Ball
fortunes = ["Yes, definitely.", "No, never.", "Ask again later.", "Cannot predict now.", "Don't count on it.", "Most likely.", "Outlook not so good.", "You may rely on it.", "Reply hazy, try again.", "Concentrate and ask again."]

random_fortune = random.choice(fortunes)
print("Magic 8-Ball says: " + random_fortune)

    #Task 3: The Card Picker
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
random_card = [random.choice(suits),random.choice(ranks)]
user = str(input("Guess the suit or rank: "))
if user in random_card:
    print("You are Correct!")
else:
    print("Better luck nect time!")