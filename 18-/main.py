###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random

import colorgram
import turtle as t
from turtle import Screen

tim = t.Turtle()

t.colormode(255)

#getting colours frim image
rgbcolors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color = (r,g,b)
    rgbcolors.append(color)

print(rgbcolors)

# tim.setpos(-200,-200)
#
#
# for i in range(6):
#     tim.sety(50 * (i-1))
#     tim.setx(-100)
#     for i in range(10):
#         tim.penup()
#         tim.dot(10,random.choice(rgbcolors))
#         tim.forward(50)
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100
tim.speed(10)


for dot_count in range(1, num_of_dots + 1):
    tim.dot(20,random.choice(rgbcolors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()