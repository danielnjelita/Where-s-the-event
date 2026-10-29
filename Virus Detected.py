from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus")

button = Button(text="Click me!", command=msg)
button.place(x=40, y=80)

root.mainloop()