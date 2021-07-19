from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for x in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)

num = 0


def style_turtle(turtle):
    global num
    turtle.color(colors[num])
    num += 1


y_axis = -230
x_axis = -125


def starting_pos(turtle):
    turtle.penup()
    global x_axis
    global y_axis
    for each in turtles:
        x_axis += 5
        turtle.goto(y_axis,x_axis)


for each in turtles:
    style_turtle(each)
    starting_pos(each)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            is_race_on = False
            if winning_colour == user_bet:
                print(f"You've won! The winning turtle is {winning_colour}!")
            else:
                print(f"You lost! The winning turtle is {winning_colour}!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()