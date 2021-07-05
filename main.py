# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_values = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r,g,b)
#     rgb_values.append(rgb_tuple)
# print(rgb_values)

from turtle import Turtle,Screen
import random
import turtle as t

t.colormode(255)
tim = Turtle()
tim.speed('fastest')
color_list = [(21, 114, 173), (142, 163, 184), (204, 137, 166), (190, 173, 17), (145, 17, 32), (238, 213, 62), (67, 24, 31), (17, 138, 59), (219, 161, 88), (122, 71, 100), (49, 29, 26), (197, 65, 28), (7, 107, 64), (227, 169, 197), (240, 78, 29), (29, 177, 84), (21, 172, 188), (243, 214, 4), (110, 192, 140), (182, 94, 115), (35, 37, 46), (188, 182, 213), (157, 206, 215), (240, 168, 154), (147, 215, 171), (127, 32, 26)]

tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.pendown()
tim.left(135)

for _ in range(10):
    for _ in range(10):
        tim.dot(15, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()


screen = Screen()
screen.exitonclick()
