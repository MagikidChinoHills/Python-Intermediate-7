#HW 4
import tkinter as tk
import random
root = tk.Tk()
root.title("HW")
canvas = tk.Canvas(root, width=1000, height=1000, bg = "white")
canvas.pack()
rec1 = canvas.create_rectangle(220, 152, 572, 57, fill="black")
rec2 = canvas.create_rectangle(100, 150, 75, 250, fill="blue")
ball = canvas.create_oval(390, 190, 410, 210, fill="red")
buttont = canvas.create_text(175, 700, text="Change color", fill="black", font=("Courier New", 24, "bold"))
x1,y1,x2,y2 = canvas.bbox(buttont)
margin = 5
button = canvas.create_rectangle(x1 - margin,y1 - margin,x2 + margin,y2 + margin, fill="gray")
canvas.tag_lower(button, buttont)
ball_dx = 15
ball_dy = 15
def moveball():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)
    if ball_pos[1] <= 0 or ball_pos[3] >= 1000:
        ball_dy = -ball_dy
    if ball_pos[0] <= 0 or ball_pos[2] >= 1000:
        ball_dx = -ball_dx
    root.after(50, moveball)
for i in range(45):
    canvas.move(rec1, -9, 0)
    canvas.move(rec2, 9, 0)
moveball()
def ccolors(event):

    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    new_color = random.choice(colors)
    canvas.itemconfigure(rec1, fill=new_color)
canvas.tag_bind(buttont, "<Button-1>", ccolors)
canvas.tag_bind(button, "<Button-1>", ccolors)
