# Classes and Objects

# A Class allows you to classify and group similar objects together
# Methods are functions inside a class. You can only call them on an object created from its class.
# Magic Method (__init__ ) define instance variables inside
# Every object is an instance of a class
# Instance vraibles are variables that belong to a object

# Create Class
class BagOfOranges:
    def __init__(self, c, s):
        self.color = c
        self.size = s
        
# Create an object / instance of class
orange1 = BagOfOranges('Bright Orange', 'Medium')
print(orange1)
print(orange1.color)
print(orange1.size)

# Change instance variable value
orange1.color = 'Dark Orange'
print(orange1.color)

# Create class
class Dog:
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age
        
    # Create method
    def bark(self):
        print("woof")
        
cavapoo = Dog('Cavapoo', 'Brown', 2)
print(cavapoo)
print(cavapoo.breed)
print(cavapoo.color)
print(cavapoo.age)
cavapoo.bark()
