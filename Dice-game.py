# Dice Game

import random
import math

# Ask if there are two players or one player playing against the computer
while True:
    try:
        num_of_players = int(input("Do you want to play a one-player or two-player game? Please type 1 or 2: "))
        print("You chose a {} player game".format(num_of_players))
        break
    except ValueError:
        print("Oops!  Thats not a valid answer. please try again...")

# Ask player for their chosen name
player1 = input("Player what would like to be called? ")

# Set player 2 default as computer
player2 = "Computer"

# If the players want to play with 2 players ask player 2 for their name
if num_of_players == 2:
    player2 = input("Player 2 what you like to be called? ")

# Print the players names
print("Let's start playing {} and {}!".format(player1, player2))

# Create a roll dice function
def roll_dice():
    return random.randint(1, 6)

# Set player 1's dice rolls and total
p1_roll_one = roll_dice()
p1_roll_two = roll_dice()
p1_total_roll = p1_roll_one + p1_roll_two

# Print the roll results to the player
print("{} you rolled a {} and a {} to create a total of {}".format(player1, p1_roll_one, p1_roll_two, p1_total_roll))

# Set player 2's dice rolls and total
p2_roll_one = rollDice()
p2_roll_two = rollDice()
p2_total_roll = p2_roll_one + p2_roll_two

# Print the roll results to the player
print("{} rolled a {} and a {} to create a total of {}".format(player2, p2_roll_one, p2_roll_two, p2_total_roll))

# Work out who wins and display winner
if p1_total_roll > p2_total_roll:
    print("{} wins!".format(player1))
elif p2_total_roll > p1_total_roll:
    print("{} wins!".format(player2))
else:
    print("It's a draw!")
