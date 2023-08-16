from turtle import Turtle, Screen
import random

screen = Screen()
# screen.reset()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")

colors = ["red", "brown", "blue", "green", "pink", "orange"]
y_positons = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.setposition(-230, y_positons[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
     
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} turtle is the winner")
            else:
                print(f"you have lost! The {winning_color} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
