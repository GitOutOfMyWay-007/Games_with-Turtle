from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    # tim.left(10)
    # tim.forward(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_right():
    # tim.right(10)
    # tim.forward(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()


def reset_to_center():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")  # we didn't include '()' after the func 'move_forward()'
# because '()' will cause the function to trigger there itself, but we are triggering func after space
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=reset_to_center, key="r")

screen.exitonclick()


# # MAKING THE TURTLE RACE GAME
#
# # making 7 turtles in the order of rainbow (vibgyor)
#
# v = Turtle()
# v.shape("turtle")
# v.color("violet")
# v.penup()
# v.setpos(-370, 150)
# v.pendown()
#
#
# i = Turtle()
# i.shape("turtle")
# i.color("indigo")
# i.penup()
# i.setpos(-370, 100)
# i.pendown()
#
#
# b = Turtle()
# b.shape("turtle")
# b.color("blue")
# b.penup()
# b.setpos(-370, 50)
# b.pendown()
#
#
# g = Turtle()
# g.shape("turtle")
# g.color("green")
# g.penup()
# g.setpos(-370, 0)
# g.pendown()
#
#
# y = Turtle()
# y.shape("turtle")
# y.color("yellow")
# y.penup()
# y.setpos(-370, -50)
# y.pendown()
#
#
# o = Turtle()
# o.shape("turtle")
# o.color("orange")
# o.penup()
# o.setpos(-370, -100)
# o.pendown()
#
#
# r = Turtle()
# r.shape("turtle")
# r.color("red")
# r.penup()
# r.setpos(-370, -150)
# r.pendown()
#
#
# screen = Screen()
# screen.setup(width=780, height=650)
# turtle.penup()
# turtle.goto(-340, -325)
# turtle.pendown()
# turtle.goto(-340, 325)
# turtle.goto(340, 325)
# turtle.goto(340, -325)
# turtle.goto(-340, -325)
# turtle.penup()
#
# screen.exitonclick()
