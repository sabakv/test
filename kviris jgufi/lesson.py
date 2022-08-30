from turtle import *
def build_house():

    speed(2)

    #კვადრატის დახატვა
    shape("turtle")
    color("red")
    begin_fill()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90) 
    end_fill()
    #სახურავის დახატვა
    begin_fill()
    color("green")
    left(90)
    forward(100)
    right(30)
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    left(90)
    forward(100)
    color("red")

    left(90)
    forward(50)
    color("red")
    color("black")

    begin_fill()

    left(90)

    forward(25)
    right(90)
    forward(10)
    right(90)
    forward(25)
    left(90)

    end_fill()



    end_fill()
    exitonclick()




build_house()
