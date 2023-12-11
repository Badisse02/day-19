import turtle
from turtle import *
from random import *

is_race_on = False
turtle.colormode(255)
s = Screen()
s.setup(500, 400)
u_bet = s.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tur = []
x1 = -230
y1 = -140

for i in range(6):
    y1 += 40
    tur.append(Turtle(shape="turtle"))
    tur[i].color(colors[i])
    tur[i].penup()
    tur[i].goto(x1, y1)

if u_bet:
    is_race_on = True

while is_race_on:
    for turtle in tur:
        if turtle.xcor() >= 230:
            winning_col = turtle.pencolor()
            if winning_col == u_bet:
                print(f"You've win! The {winning_col} is the winner!")
            else:
                print(f"You've lost! The {winning_col} is the winner!")
            is_race_on = False
            break
        rand_dis = randint(0,10)
        turtle.forward(rand_dis)


s.listen()
s.exitonclick()
