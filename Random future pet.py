# What animal should you get and what should their name be?
# Random name and animal generator

import random

name = ['Bob', 'Charlie', 'Snuggles', 'Fluffy', 'Noodles', 'Buddy', 'Hugo', 'Frank', 'Bella', 'Rosie']
animal = ['Hedgehog', 'Snake', 'Ferret', 'Rabbit', 'Dog', 'Fish', 'Cat', 'Bearded Dragon', 'Gecko', 'Tortoise', 'Frog', 'Rat', 'Hamster']

chosen_name = random.choice(name)
chosen_animal = random.choice(animal)

print("You should get a {} and call them {}!".format(chosen_animal, chosen_name))

personality = ['cheeky', 'grumpy', 'fiesty', 'happy', 'silly', 'socialable', 'quiet', 'shy', 'anxious', 'intelligent']

chosen_personality = random.choice(personality)

print("Their personality will be... {}".format(chosen_personality))

color = ['brown', 'white', 'orange', 'black', 'black and white', 'brown and white', 'grey', 'brown, black and white', 'tan', 'blue!', 'yellow with purple spots!']

chosen_color = random.choice(color)

print("And they will also be {}".format(chosen_color))
