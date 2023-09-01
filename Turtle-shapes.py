from turtle import Turtle, Screen
import random

t = Turtle()

colors = ["red", "purple", "yellow", "green"]

def draw_shape(sides):
  angle = 360 / sides
  for i in range(sides):
    t.forward(75)
    t.right(angle)


# create shapes with 3-9 sides
# use a random color for the pen choice
for i in range(3,10):
  t.color(random.choice(colors))
  draw_shape(i)


# create the window
screen = Screen()
screen.exitonclick()
