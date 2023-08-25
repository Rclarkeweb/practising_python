# Cuteness Comparison

import random

# list of animals and data
animals = [
    {
        'species': 'Ardvark',
        'cuteness': 7
    },
    {
        'species': 'Pangolin',
        'cuteness': 9
    },
    {
        'species': 'Frog',
        'cuteness': 5
    },
    {
        'species': 'Snake',
        'cuteness': 4
    },
    {
        'species': 'Spider',
        'cuteness': 1
    },
    {
        'species': 'Rabbit',
        'cuteness': 8
    },
    {
        'species': 'Beetle',
        'cuteness': 2
    },
    {
        'species': 'Sloth',
        'cuteness': 6
    },
]

# function to pick a random animal
def pick_data(data):
    chosen = random.choice(data)
    return chosen
    
# function to check if guess is correct
def check_answer(guess, a, b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"

# set score variable
score = 0

# set if game should continue 
game_should_continue = True

# pick a random animal for option b
second_animal = pick_data(animals)

while game_should_continue:
    # assign two animals to two variables
    first_animal = second_animal
    second_animal = pick_data(animals)
    # if the animals picked are the same choose another
    if first_animal == second_animal:
        while first_animal == second_animal:
            second_animal = pick_data(animals)
    
    # print out animals to user
    print("\n---------------------------------\n\nWho do you think is cuter? Is it:")
    print(f"\nA: {first_animal['species']}")
    print("\n VS \n")
    print(f"B: {second_animal['species']}\n")
    
    # ask user for their guess
    guess = input("Type 'a' or 'b' here: ").lower()
    
    # set two variables to the animals cuteness levels
    first_animal_cuteness = first_animal['cuteness']
    second_animal_cuteness = second_animal['cuteness']

    is_correct = check_answer(guess, first_animal_cuteness, second_animal_cuteness)

    # check if user is correct and if so adjust score
    if is_correct == True:
        score += 1
        print(f"Correct! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
      
