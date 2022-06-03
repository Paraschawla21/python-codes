from turtle import Turtle, Screen  # importing Turtle (and Screen) class from turtle module  # Pascal case
timmy = Turtle() # making an object of name timmy
print(timmy)
timmy.shape("turtle")
timmy.color("red")   # timmy.color("black", "red")
timmy.forward(100)
my_screen = Screen()
# print(my_screen.canvheight)  # object.attribute
my_screen.exitonclick()   # object.method