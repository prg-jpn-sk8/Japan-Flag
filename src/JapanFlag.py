from turtle import *

bgcolor("grey")

hideturtle()

penup()
goto(-215, -245)
pendown()

pencolor("white")

begin_fill()
for x in range(2):
    fillcolor("white")
    fd(420)
    circle(100, 90)
    fd(300)
    circle(100, 90)
end_fill()
penup()
goto(0, -75)
pendown()
begin_fill()
fillcolor("red")
circle(100)
end_fill()
done()