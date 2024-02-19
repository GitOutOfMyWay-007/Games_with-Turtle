# MAKING THE TURTLE RACE GAME

# making 7 turtles in the order of rainbow (vibgyor)

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Welcome to the turtle race!", prompt="Please select a turtle color "
                                                                        "(PS: Each turtle is a color from the rainbow.)")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_position = [150, 100, 50, 0, -50, -100, -150]
all_turtles = []  # Making an empty list to append all the created turtles here

# Making 7 turtles at once using for loop
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU WIN!! The {winning_color} turtle is the winner")
            else:
                print(f"YOU LOSE:( The {winning_color} turtle won. Better Luck Next Time ")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

# # making each tutle individually is not efficient

# v = Turtle(shape= "turtle")
# v.color("violet")
# v.penup()
# v.setpos(-230, 150)
# v.pendown()
#
# i = Turtle(shape= "turtle")
# i.color("indigo")
# i.penup()
# i.setpos(-230, 100)
# i.pendown()
#
# b = Turtle(shape= "turtle")
# b.color("blue")
# b.penup()
# b.setpos(-230, 50)
# b.pendown()
#
# g = Turtle(shape= "turtle")
# g.color("green")
# g.penup()
# g.setpos(-230, 0)
# g.pendown()
#
# y = Turtle(shape= "turtle")
# y.color("yellow")
# y.penup()
# y.setpos(-230, -50)
# y.pendown()
#
# o = Turtle(shape= "turtle")
# o.color("orange")
# o.penup()
# o.setpos(-230, -100)
# o.pendown()
#
# r = Turtle(shape= "turtle")
# r.color("red")
# r.penup()
# r.setpos(-230, -150)
# r.pendown()

# screen.exitonclick()


