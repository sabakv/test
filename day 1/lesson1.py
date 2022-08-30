from operator import le
from turtle import *

color("red")
width(10)

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

left(90)
forward(200)

color("blue")

begin_fill()
right(30)
forward(200)

right(120)
forward(200)

end_fill()

color("red")

penup()
right(30)
forward(200)

right(90)
forward(70)
pendown()

color("black")

begin_fill()
right(90)
forward(70)

left(90)
forward(50)

left(90)
forward(70)

left(90)
forward(50)

end_fill()

penup()
left(90)
forward(100)
pendown()

exitonclick()