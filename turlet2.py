import turtle

window = turtle.Screen()
t = turtle.Pen()

t.speed(0)

t.penup()
t.goto(-250,60)
t.pendown()

t.pensize(3)
t.circle(60,-200)
t.circle(60,200)
t.penup()
t.goto(-250-15,-60)
t.pendown()
t.circle(60,180)
t.penup()
t.goto(-125,-60)
t.pendown()
t.circle(50)

window.exitonclick()