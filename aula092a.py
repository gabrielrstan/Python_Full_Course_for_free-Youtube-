from tkinter import *
import time
from aula092b import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 2, 1.4, 'white')
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, 'yellow')
basket_ball = Ball(canvas, 0, 0, 125, 8, 7, 'orange')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()