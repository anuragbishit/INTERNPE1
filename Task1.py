# TASK1= Make a Digital clock With the help of Python.
from tkinter import Tk, Label
import time

master = Tk()
master.title("Digital clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time) 

clock = Label(master, font=("Calibri", 90), bg="grey", fg="white")
clock.pack()

get_time()

master.mainloop()
