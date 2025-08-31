#1
import turtle
import random

t = turtle.Turtle()
t.speed(0)

for _ in range(100):  
    distance = random.randint(10, 50)   
    angle = random.randint(0, 180)      
    t.forward(distance)
    t.left(angle)


turtle.done()



#2
import turtle
import random

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

for _ in range(100):
    distance = random.randint(10, 50)
    angle = random.randint(0, 180)
    t.color(random.choice(colors))   
    t.forward(distance)
    t.left(angle)

turtle.done()




#3.
import turtle
import random

t = turtle.Turtle()
t.speed(0)

def spirograph(angle):
    for _ in range(int(360 / angle)):
        radius = random.randint(50, 150)  
        t.circle(radius)
        t.left(angle)

spirograph(10)  
turtle.done()



#4
import turtle

t = turtle.Turtle()
t.speed(0)

def spirograph(angle, radius, color):
    t.color(color)
    for _ in range(int(360 / angle)):
        t.circle(radius)
        t.left(angle)

colors = ["red", "blue", "green"]

angles = [5, 10, 15]
for i in range(3):
    spirograph(angles[i], 100, colors[i])
    t.penup()
    t.forward(200)   
    t.pendown()

turtle.done()



#5
import turtle
import random

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

def random_spirograph(angle):
    for _ in range(int(360 / angle)):
        radius = random.randint(50, 150)   
        t.color(random.choice(colors))   
        t.circle(radius)
        t.left(angle)

random_spirograph(10)
turtle.done()
