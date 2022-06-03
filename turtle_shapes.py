from turtle import Turtle, Screen
import random
colors = ["red", "blue", "green", "white", "black", "pink", "purple", "seagreen"]
t = Turtle()
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for ele in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(ele)
s = Screen()
s.exitonclick()