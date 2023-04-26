# Number Guessing Game
import random

print('Lets Guess the Number!')
print('It will be a number between 1 and 30')

def guessNumber():
    number = random.randint(1,30)
    guess = 0
    while guess != number:
        guess = int(input('What is your guess? '))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
    print('Congratulations! You guessed the random number: {}'.format(number))

guessNumber()
