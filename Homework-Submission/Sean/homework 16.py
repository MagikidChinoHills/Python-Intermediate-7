import turtle
import random

#color list
colors=["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan"]

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_pentagon(t, length):
    t.color(random.choice(colors))
    t.begin_fill()
    for _ in range(5):
        t.forward(length)
        t.right(72)
    t.end_fill()

def draw_grid_of_squares(t, rows, cols, size):
    gap = 10
    start_x = t.xcor()
    start_y = t.ycor()

    for row in range(rows):
        for col in range(cols):
            t.color(random.choice(colors))
            t.begin_fill()
            draw_square(t, size)
            t.end_fill()

            t.penup()
            t.forward(size + gap)
            t.pendown()
        
        t.penup()
        t.goto(start_x, start_y - (row + 1) * (size + gap))
        t.pendown()

def draw_spiral_stars(t, num_stars):
    size = 10
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for _ in range(num_stars):
        t.color(random.choice(colors))
        t.begin_fill()
        draw_star(t, size)
        t.end_fill()

        size += 3
        t.right(15)
        t.penup()
        t.forward(10)
        t.pendown()

def draw_random_art(t, num_shapes):
    shape_functions = [draw_square, draw_star, draw_pentagon]

    for _ in range(num_shapes):
        shape = random.choice(shape_functions)
        t.penup()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.goto(x, y)
        t.setheading(random.randint(0, 360))
        t.pendown()
        shape(t, random.randint(20, 60))


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    tim = turtle.Turtle()
    tim.speed(0)

    draw_random_art(tim, num_shapes=40)

    screen.mainloop()
