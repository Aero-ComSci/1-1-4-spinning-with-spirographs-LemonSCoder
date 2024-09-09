import math
import random
import turtle
colors = ["light slate gray", "alice blue", "light steel blue", "cornflower blue", "royal blue", "navy", "midnight blue", "light blue", "powder blue", "light sky blue", "azure", "light cyan", "pale turquoise","turquoise", "aquamarine"]
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(20)
turtle.screensize(800, 800, random.choice(colors))
concentric_number = 120
while concentric_number <= 600:
    spiral_turtle.pencolor(random.choice(colors))
    spiral_turtle.pensize(15)
    spiral_turtle.penup()
    spiral_turtle.goto(0, 0)
    spiral_turtle.right(90)
    spiral_turtle.forward(concentric_number)
    spiral_turtle.pendown()
    spiral_turtle.right(90)
    spiral_turtle.penup()
    spiral_turtle.goto(concentric_number, 0)
    spiral_turtle.pendown()
    turn_count = 0
    while turn_count < 4:
        spiral_turtle.forward(concentric_number)
        spiral_turtle.right(90)
        turn_count += 1
    concentric_number += 120




