import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)

# List of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "white"]

# Draw a colorful spiral
for i in range(100):
    t.color(random.choice(colors))  # Pick a random color
    t.forward(i * 3)  # Move forward
    t.right(59)  # Turn right
    t.forward(i * 2)  # Move forward
    t.right(61)  # Turn right

# Hide the turtle and finish
t.hideturtle()
turtle.done()
