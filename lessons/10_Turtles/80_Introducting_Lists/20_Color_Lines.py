"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
    ... # Your code here
    tina.color(color)
    tina.forward(100)
    tina.right(90)


# 2) Make another square, but put the colors in reverse order, using a negative index. 

 # Your code here

tina.goto(150, 150)

for i in range(3, -1, -1) :
    tina.color(colors[i])
    tina.forward(100)
    tina.right(90)

turtle.exitonclick()                     # Close the window when we click on it