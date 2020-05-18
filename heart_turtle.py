import time
import turtle

def hart_arc():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

def move_pen_position(x,y):
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.showturtle()

love='520'
people="--by Ling Duye"

turtle.setup(width=800,height=500)
turtle.color('pink','pink')
turtle.pensize(3)
turtle.speed(1)

move_pen_position(0,-180)
turtle.left(140)
turtle.begin_fill()
turtle.forward(224)
hart_arc()
turtle.left(120)
hart_arc()
turtle.forward(224)
time.sleep(0.8)
turtle.end_fill()

move_pen_position(0,0)
turtle.color('#CD5C5C','pink')
time.sleep(0.5)
turtle.write(love)

if people!='':
    turtle.color('red','pink')
time.sleep(0.2)
move_pen_position(180,-180)

turtle.hideturtle()
turtle.write(people)

window=turtle.Screen()
window.exitonclick()