# Dice Game

import random
import math

# Ask if there are two players or one player playing against the computer
while True:
    try:
        numOfPlayers = int(input("Do you want to play a one-player or two-player game? Please type 1 or 2: "))
        print("You chose a {} player game".format(numOfPlayers))
        break
    except ValueError:
        print("Oops!  Thats not a valid answer. please try again...")

# Ask player for their chosen name
player1 = input("Player what would like to be called? ")

# Set player 2 default as computer
player2 = "Computer"

# If the players want to play with 2 players ask player 2 for their name
if numOfPlayers == 2:
    player2 = input("Player 2 what you like to be called? ")

# Print the players names
print("Let's start playing {} and {}!".format(player1, player2))

# Create a roll dice function
def rollDice():
    return random.randint(1, 6)

# Set player 1's dice rolls and total
p1rollOne = rollDice()
p1rollTwo = rollDice()
p1totalRoll = p1rollOne + p1rollTwo

# Print the roll results to the player
print("{} you rolled a {} and a {} to create a total of {}".format(player1, p1rollOne, p1rollTwo, p1totalRoll))

# Set player 2's dice rolls and total
p2rollOne = rollDice()
p2rollTwo = rollDice()
p2totalRoll = p2rollOne + p2rollTwo

# Print the roll results to the player
print("{} rolled a {} and a {} to create a total of {}".format(player2, p2rollOne, p2rollTwo, p2totalRoll))

# Work out who wins and display winner
if p1totalRoll > p2totalRoll:
    print("{} wins!".format(player1))
elif p2totalRoll > p1totalRoll:
    print("{} wins!".format(player2))
else:
    print("It's a draw!")
