import math
import random
import turtle
background_colors = ["dim gray", "black", "slate gray", "midnight blue", "dark slate gray"]
colors = ["light slate gray", "alice blue", "light steel blue", "cornflower blue", "royal blue", "navy", "midnight blue", "light blue", "powder blue", "light sky blue", "azure", "light cyan", "pale turquoise","turquoise", "aquamarine", "pale green", "spring green", "green yellow", "chartreuse", "yellow green", "medium violet red", "dark magenta", "violet", "magenta", "thistle", "plum", "orchid", "medium orchid", "blue violet", "medium purple", "lavender", "medium slate blue"]
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(20)
turtle.screensize(800, 800, random.choice(background_colors))
concentric_number = 160
while concentric_number <= (160 * 5):
    spiral_turtle.pencolor(random.choice(colors))
    spiral_turtle.pensize(15)
    spiral_turtle.penup()
    spiral_turtle.goto((concentric_number / 2), ((concentric_number) / 2))
    spiral_turtle.forward(-(concentric_number))
    spiral_turtle.pendown()
    turn_count = 0
    while turn_count < 4:
        spiral_turtle.forward(concentric_number)
        spiral_turtle.right(90)
        turn_count += 1
    concentric_number += 160
turtle.done()
