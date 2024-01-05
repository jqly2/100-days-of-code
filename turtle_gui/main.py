import turtle as player
from turtle import Screen
import random as random
import hirstcp as list
# code use to extract the color palette in 'hirstcp.py'
# import colorgram as cg
# import os

# img = os.path.join('100-days-of-code/turtle_gui/', "img.jpg")

# rgb_colors = []
# colors = cg.extract(img, 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
    
# print(rgb_colors)

player.shape("triangle")
player.teleport(-400,-400)
tp_x = player.xcor()

screen = Screen()
screen.colormode(255)
screen.screensize(400,400)

def movement_x(pos_x):
    while pos_x != 400:

        pos_x = pos_x + 50
        if pos_x == 400 and player.ycor() == 400:
            player.dot(25, random.choice(list.color))
            player.hideturtle()
            break
        else:
            if pos_x == 400:
                pos_x = restart(player.ycor())
            else:
                player.dot(25, random.choice(list.color))
                player.teleport(pos_x)

def restart(pos_y):
    player.dot(25, random.choice(list.color))
    player.teleport(-400, pos_y + 50)
    return -400

movement_x(tp_x)

screen.exitonclick()
