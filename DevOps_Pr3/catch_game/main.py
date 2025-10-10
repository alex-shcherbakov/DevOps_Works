from tkinter import *
import random
import time

from DevOps_Pr3.catch_game.Catcher import Catcher
from DevOps_Pr3.catch_game.Score import Score

tk = Tk()
tk.title("Гра: Ловець!")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400,
                bd=0, highlightthickness=0)
canvas.pack()

score = Score(canvas)
catcher = Catcher(canvas, 'blue', score)
tk.update()
time.sleep(1)
