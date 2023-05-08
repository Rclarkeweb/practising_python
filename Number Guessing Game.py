# Number Guessing Game
import random

print('Let\'s Play: Guess the Number!')
print('The number will be between 1 and 30')

def guessNumber():
    number = random.randint(1,30)
    guess = 0
    attempts = 0
    while guess != number:
        guess = int(input('What is your guess? '))
        attempts += 1
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
    print('Congratulations! You guessed the random number: {}! It took you {} guesses!'.format(number, attempts))

guessNumber()
