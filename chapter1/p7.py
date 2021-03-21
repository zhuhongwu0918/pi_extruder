import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("my")

aLabel = ttk.Label(win,text="A Label")
aLabel.grid(column=0,row=0)  #网格布局

def clickeMe():
    action.configure(text="**I have been Clicked!**")
    aLabel.configure(foreground='red')
action = ttk.Button(win, text="Click Me!",command=clickeMe)
action.grid(column=1,row=1)
win.mainloop()