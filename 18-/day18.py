import turtle as t
from turtle import Screen
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("DarkSlateGray4")
t.colormode(255)
# for _ in range (10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()#

# random walk
def rand_col():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


directions = [0,90,180,270]

# for i in range(200):
#     timmy.forward(30)
#     timmy.right(random.choice(directions))
#     timmy.pencolor(rand_col())
#     timmy.speed(10)

# spirograph
for i in range(200):
    timmy.speed(10)
    timmy.circle(100)
    timmy.left(10)
    timmy.pencolor(rand_col())



screen = Screen()
screen.exitonclick()