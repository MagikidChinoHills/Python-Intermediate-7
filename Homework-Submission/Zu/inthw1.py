#1
import turtle

t = turtle.Turtle()

for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()

#2
import turtle

t = turtle.Turtle()

for _ in range(6):
    t.forward(80)
    t.left(60)

turtle.done()



#3
import turtle


t = turtle.Turtle()

t.fillcolor("blue")
t.begin_fill()


for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(75)
    t.left(90)

t.end_fill()
turtle.done()

#4

import turtle

t = turtle.Turtle()

t.fillcolor("red")
t.begin_fill()

for _ in range(5):
    t.forward(100)
    t.right(144)

t.end_fill()
turtle.done()

#5

import turtle

t = turtle.Turtle()

t.circle(100)

turtle.done()

