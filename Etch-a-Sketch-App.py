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
