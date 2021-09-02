'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
ye=turtle.Turtle()
ye.color('black')
ye.shape('turtle')

ye.penup()
ye.goto(0,-150)
ye.pendown()
ye.circle(120)
ye.penup()
ye.right(90)
ye.forward(10)
ye.pendown()
ye.left(90)
ye.forward(130)
ye.left(90)
ye.forward(260)
ye.left(90)
ye.forward(300)
ye.left(90)
ye.forward(260)
ye.left(90)
ye.forward(170)
ye.penup()
ye.left(180)
ye.forward(130)
ye.right(90)
ye.pendown()
ye.forward(260)
ye.penup()
ye.goto(20,-30)
ye.pendown()
ye.circle(20)
ye.penup()
ye.right(90)
ye.forward(120)
ye.left(90)
ye.forward(40)
ye.pendown()
ye.left(90)
ye.forward(80)
ye.left(90)
ye.forward(80)
ye.left(90)
ye.forward(80)
ye.left(90)
ye.forward(80)

#yoda.pencolor('#00FF00')


ye.write('Will Fuchs',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
