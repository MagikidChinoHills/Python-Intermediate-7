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
