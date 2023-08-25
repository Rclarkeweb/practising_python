# Guess the animal species
import random

# Create list of animals
word_list = ["ostrich", "mouse", "dog", "camel", "rabbit", "pangolin", "whale", "elephant", "platypus",
             "duck", "nightjar", "otter", "dolphin", "wolf"]

# Generate a random animal
chosen_word = random.choice(word_list)

# Find the length of the chosen word
word_length = len(chosen_word)

# Create an empty list
display = []

# Print out blank spaces
for i in range(word_length):
    display += "_"

print(f"{' '.join(display)}\n")

# Set the variable as false for the while loop
end_game = False
attempts = 0

# create while loop to loop through game until blanks are filled
while not end_game:

    # Ask user for a letter and change it to lowercase
    guess = input("Choose a letter: ").lower()

    # Add the letter to the position in the word
    for position in range(word_length):

        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

            print(f"\n{guess} is in the word")
            attempts += 1

    if guess not in chosen_word:
        print(f"\n{guess} isn't in the word, guess again!")
        attempts += 1

    # Display the result
    print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_game = True

        print(f"You win! The word was {chosen_word} \n You guessed it in {attempts} attempts!")
