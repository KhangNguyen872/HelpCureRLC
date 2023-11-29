import turtle
import time

print(time.asctime())

window = turtle.Screen()

t = turtle.Pen()

'''
def draw_shape(size, sides):
    for x in range(0,sides):
        t.speed(0)
        t.fd(size)
        t.lt(360/sides)

user_size = int(input("What size should it be?: "))
user_sides = int(input("How many sides?: "))


draw_shape(user_size,user_sides)
'''

t.penup()
t.goto(0,0)
t.pendown()
t.speed(0)

def draw_shape(size,sides):
    for x in range(0,180):
        for x in range(0,sides):
            t.fd(size)
            t.lt(360/sides)
        t.lt(2)

user_sides = int(input("How many sides?: "))
user_size = int(input("What size?: "))

draw_shape(user_size,user_sides)

window.exitonclick()