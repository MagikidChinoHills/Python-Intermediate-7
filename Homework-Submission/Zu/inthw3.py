import turtle

t = turtle.Turtle()
t.speed(0)
length = 1
for i in range (50):
  t.forward(length)
  t.right(30)
  length +=1
t.done()




#2
t = turtle.Turtle

def draw_diamond(size):
  for i in range(2):
    t.forward(size)
    t.left(60)
    t.forward(size)
    t.left(120)
for i in range (12):
  draw_diamond(100)
  t.left(30)
t.done()




#3

import turtle as t


t.penup()
t.goto(0,-100)
t.pendown()
t.speed(0)
t.color("blue","red")
t.pensize(10)
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50,200)
t.right(140)
t.circle(50,200)
t.forward(133)
t.end_fill()

t.done()








#4
t.color("purple")

def draw_petals():
  for i in range(2)
  t.circle(100,60)
  t.left(120)
  t.circle(100,60)
  t.left(120)

for i in range(36):
  draw_pedals()
  t.right(10)
t.done()



#5

colors = ["red","blue","green","yellow","purple","orange","pink"]
def draw_square(size,depth):
  if depth == 0:
    return 
  t.pencolor(random.choice(colors))
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.penup()
  t.forward(size/4)
  t.right(90)
  t.forward(size/4)
  t.left(90)
  t.pendown()
  draw_square(size/2. depth-1)

draw_square(200,5)

t.done()
