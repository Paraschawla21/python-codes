# from turtle import *
from turtle import Turtle, Screen
turtle_object = Turtle()
turtle_object.shape("turtle")
turtle_object.color("red")
# for _ in range(4):
#     turtle_object.forward(100)
#     turtle_object.right(90)


# import heroes
# print(heroes.gen())
for _ in range(12):
    turtle_object.forward(10)
    turtle_object.penup()
    turtle_object.forward(10)
    turtle_object.pendown()

screen = Screen()
screen.exitonclick()