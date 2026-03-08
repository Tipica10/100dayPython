###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.penup()
t.colormode(255)
start = tim.setpos(-200,-200)

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

for i in range(6):
    tim.setpos(-200, -200)
    tim.sety(50 * (i-1))
    for i in range(10):
        tim.penup()
        tim.dot(10,rgbcolors[i])
        tim.forward(50)


screen = Screen()
screen.exitonclick()