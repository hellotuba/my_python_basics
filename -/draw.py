import turtle
import time
import math

# Set up the screen
screen = turtle.Screen()
screen.title("Animated Spiral")
screen.bgcolor("black")  # Set the background color to black

# Create a turtle object
drawer = turtle.Turtle()
drawer.color("white")  # Set the turtle's drawing color to white for contrast
drawer.speed(100000)  # Set the turtle's speed to the fastest

# Draw an animated spiral
radius = 1
angle = 0

drawer.penup()
drawer.goto(0, 0)  # Start at the center
drawer.pendown()

# Animate the spiral
while radius < 400000000:  # Limit the spiral size
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    drawer.goto(x, y)
    angle += 5  # Increment the angle
    radius += 0.5  # Gradually increase the radius
    time.sleep(0.01)  # Add a small delay for animation effect

# Finish
drawer.hideturtle()
turtle.done()