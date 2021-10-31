from turtle import Screen,Turtle
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-60,-30,0,30,60,90]
all_turtles=[]

for turtle_index in range(0,6):
     new_turtle=Turtle(shape="turtle")
     new_turtle.color(colors[turtle_index])
     new_turtle.penup()
     new_turtle.goto(x=-230,y=y_positions[turtle_index])
     new_turtle.pendown()
     all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            wining_color=turtle.pencolor()
            if wining_color == user_bet:
                print("you win")
            else:
                print("you lose")
                       
        rand_disntance=random.randint(0, 10)
        turtle.forward(rand_disntance)

screen.exitonclick()
