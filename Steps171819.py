#Answer to Step Seventeen.
import turtle as trtl
#Makes sure pen goes to the edge of the screen.
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1
#Runs while x is less than or equal to zero.
while (x <= 0):
  #Runs while y is less than one hundred
  while (y < 100):
    #x moves right
    x = x + move_x
    #y moves up
    y = y + move_y
    painter.goto(x,y)
  #y moves down next time
  move_y = -1
  #Runs while y is greater than zero.
  while (y > 0):
    #x moves right
    x = x + move_x
    #y moves down
    y = y + move_y
    painter.goto(x,y)
  #y goes up next time
  move_y = 1
  
wn = trtl.Screen()
wn.mainloop()

#Solution to Question Eighteen.
import turtle as trtl
#Makes sure pen goes to the edge of the screen.
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1
#Runs while x is less than zero.
while (x < 0):
  #Runs while y is less than one hundred.
  while (y < 100):
    #x moves to the right
    x = x + move_x
    #y moves up
    y = y + move_y
    painter.goto(x,y)
  #y moves down next time
  move_y = -1
  #Runs while y is greater than negative one hundred.
  while (y > (-100)):
    #x moves to the right
    x = x + move_x
    #y moves down
    y = y + move_y
    painter.goto(x,y)
  #y moves up next time
  move_y = 1
  #Runs while y is less than one hundred.
  while (y < (100)):
    #x moves to the right
    x = x + move_x
    #y moves up
    y = y + move_y
    painter.goto(x,y)
  #y moves up next time
  move_y = 1
#Makes sure pen goes to the edge of the screen.
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1
#Runs while x is less than or equal to zero
while (x <= 0):
  #Runs while x is less than negative one hundred
  while (x < (-100)):
    #x moves right
    x = x + move_x
    #y moves down
    y = y - move_y
    painter.goto(x,y)
  #y moves up next time
  move_y = 1
  #Runs while y is less than one hundred
  while (y < 100):
    #x moves right
    x = x + move_x
    #y moves up
    y = y + move_y
    painter.goto(x,y)
  #y moves up next time
  move_y = 1
  #Runs while x is less than four hundred
  while (x < 400):
    #x moves right
    x = x + move_x
    #y moves down
    y = y - move_y
    painter.goto(x,y)

wn = trtl.Screen()
wn.mainloop()

#Solution to Step Nineteen
import turtle as trtl

painter = trtl.Turtle()
#Will run infinitely since nothing equates this while loop to false and there is no break in the loop.
while True:
  x = -200
  y = 0
  move_x = 1
  move_y = 1
  #Runs while x is less than zero (will happen continuously since x resets to being equal to negative two hundred every time the loop runs again (infinitely)
  while (x < 0):
    #Makes sure pen goes to the edge of the screen.
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()
    #Runs while y is less than one hundred.
    while (y < 100):
      #x moves right
      x = x + move_x
      #y moves up
      y = y + move_y
      painter.goto(x,y)
    #y moves down next time
    move_y = -1
    #Runs while y is greater than negative one hundred
    while (y > (-100)):
      #x moves right
      x = x + move_x
      #y moves up
      y = y + move_y
      painter.goto(x,y)
    #y moves up next time
    move_y = 1
    #Runs while y is less than one hundred.
    while (y < (100)):
      #x moves right
      x = x + move_x
      #y goes up
      y = y + move_y
      painter.goto(x,y)
    #y moves up next time
    move_y = 1
    
  #Makes sure pen goes to the edge of the screen.
  painter.penup()
  painter.goto(-200, 0)
  painter.pendown()

  x = -200
  y = 0
  move_x = 1
  move_y = 1
  #Runs while x is less than zero.
  while (x < 0):
    #Runs while x is less than negative one hundred.
    while (x < (-100)):
      #x moves right
      x = x + move_x
      #y moves down
      y = y - move_y
      painter.goto(x,y)
    #y moves up next time
    move_y = 1
    #Runs while y is less than one hundred
    while (y < 100):
      #x moves right
      x = x + move_x
      #y moves up
      y = y + move_y
      painter.goto(x,y)
    #y moves up next time
    move_y = 1
    #Runs while x is less than four hundred
    while (x < 400):
      #x moves right
      x = x + move_x
      #y moves down
      y = y - move_y
      painter.goto(x,y)
    #y moves down next time
    move_y = -1


wn = trtl.Screen()
wn.mainloop()
