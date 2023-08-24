# Guess The Number
import random

# Set the number of guesses allowed for each level
EASY = 15
MEDIUM = 10
HARD = 5


# generate the answer function
def generate_num():
    answer = random.randint(1,50)
    return answer


# ask user for difficulty level and save
def difficulty_level():
    level = input("Choose a difficulty. Type 'easy', 'medium, or 'hard': ")
    if level == "easy":
        return EASY
    elif level == "medium":
        return MEDIUM
    else:
        return HARD


# check if user guess is equal to answer
def check_answer(guess, attempts, answer):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")


# function to play the game
def play():
    print("Lets play Guess the Number!")
    print("I'm thinking of a number between 1 and 50.")
    # generate the answer
    answer = generate_num()
  
    # set the number of user attempts
    attempts = difficulty_level()
    print(f"You have {attempts} attempts to guess the answer")
  
    # create a loop to allow the user to keep guesing
    while attempts != 0:
        guess = int(input('Make a guess: '))
        attempts = check_answer(guess, attempts, answer)
        
        if attempts == 0:
            print(f"You've run out attempts! The answer was {answer}")
            return
        elif guess != answer:
            print(f"Guess again. You have {attempts} left.")
        else: 
            return
    
play()
