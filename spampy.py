
# python spammer
import pyautogui as pg
import time
from tkinter import *

# Function called by Button


def spamm():
    b = _input.get()
    a = no_of_time.get()
    t = time_delay.get()

    # print(b)
    time.sleep(5)

    for i in range(a):
        pg.write(b)
        time.sleep(t)
        pg.press("enter")


# Basic Lines
root = Tk()
root.geometry("500x200")
root.title("Py Spammer")

# Making lables and packing them with grid
lab = Label(text="Enter text you wanna spam:").grid(row=0, column=1)
lab = Label(text="Enter no of times:").grid(row=1, column=1)
lab = Label(text="Enter time delay:").grid(row=2, column=1)

# Inializing Variables
_input = StringVar()
no_of_time = IntVar()
time_delay = IntVar()

# Making entries
_entry = Entry(root, textvariable=_input).grid(row=0, column=2)
_no_times = Entry(root, textvariable=no_of_time).grid(row=1, column=2)
_delay = Entry(root, textvariable=time_delay).grid(row=2, column=2)

# Making Button
Button(text="Submit", command=spamm).grid(row=3, column=2)


root.mainloop()

# print(pg.position())
