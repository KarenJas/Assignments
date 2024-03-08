#7. Python's Random Game Night
    #Task 1: Dice Rolling Simulator
import random
# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

    #Task 2: Random Choice Game
user_guess = int(input("Guess: "))
dice = [1,2,3,4,5,6]
random_roll = random.choice(dice)

if user_guess == random_roll :
    print( "You are correct! :)")
else:
    print("You are Wrong :(")

    #Task 3: Shuffling a Deck
#random.shuffle() can be used to randomize an action and allow the user to play with it 
#by having them guess the output or allowing them to use it as a tool like in the dice rolling game above

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
print(deck)
random.shuffle(deck)
print(deck)
