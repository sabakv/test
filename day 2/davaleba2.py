from turtle import *


#სისწრაფე, ფერი და სისქე
speed(3)
color("blue")
width(5)


#პირველი ოთკუთხედი
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


#დიაგონალზე გადაადგილების კოდი
right(90)
penup()
goto(-300,200)
pendown()


#მეორე ოთკუთხედი
begin_fill()
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()


#სწორად გადაადგილების კოდი
penup()
left(90)
forward(400)
pendown()


#მესამე ოთკუთხედი
begin_fill()
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()


#დიაგონალზე გადაადგილების კოდი
right(90)
penup()
goto(-300,-0)
pendown()


#მეოთხე ოთკუთხედი
begin_fill()
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()



exitonclick() 