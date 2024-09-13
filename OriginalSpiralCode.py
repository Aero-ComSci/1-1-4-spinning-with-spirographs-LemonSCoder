#Imported modules to avoid errors
import math
import random
import turtle
#List of dark background colors
background_colors = ["dim gray", "black", "slate gray", "midnight blue", "dark slate gray"]
#List of square colors (in cool colors)
colors = ["light slate gray", "alice blue", "light steel blue", "cornflower blue", "royal blue", "navy", "midnight blue", "light blue", "powder blue", "light sky blue", "azure", "light cyan", "pale turquoise","turquoise", "aquamarine", "pale green", "spring green", "green yellow", "chartreuse", "yellow green", "medium violet red", "dark magenta", "violet", "magenta", "thistle", "plum", "orchid", "medium orchid", "blue violet", "medium purple", "lavender", "medium slate blue"]
spiral_turtle = turtle.Turtle()
#Speeds up drawing process
spiral_turtle.speed(20)
#Sets up the turtle screen
turtle.screensize(800, 800, random.choice(background_colors))
#The distance from one side of the square to another side of the square.
concentric_number = 160
#makes sure squares are drawn five times.
while concentric_number <= (800):
    #Ensures each square drawn is a different color.
    spiral_turtle.pencolor(random.choice(colors))
    #Makes sure each pen is at a good pen size.
    spiral_turtle.pensize(15)
    spiral_turtle.penup()
    #Allows squares with equal distances from each other and the center/edges of the screen to be drawn.
    spiral_turtle.goto((concentric_number / 2), ((concentric_number) / 2))
    spiral_turtle.forward(-(concentric_number))
    spiral_turtle.pendown()
    turn_count = 0
    #Allows each side of the square to be drawn per square.
    while turn_count < 4:
        spiral_turtle.forward(concentric_number)
        spiral_turtle.right(90)
        #Prevents an infinite loop.
        turn_count += 1
    #Prevents an infinite loop and makes sure the squares are equally distanced from each other.
    concentric_number += 160
#Makes sure turtle drawing doesn't close.
turtle.done()
