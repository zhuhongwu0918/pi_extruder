import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("my")
def clickMe(): # 2
    action.configure(text='Hello ' + name.get())
action = ttk.Button(win, text="Click Me!",command=clickMe)
# Modified Button Click Function # 1

# Position Button in second row, second column (zero-based)
action.grid(column=1, row=1)
# Changing our Label # 3
ttk.Label(win, text="Enter a name:").grid(column=0, row=0) # 4
# Adding a Textbox Entry widget # 5
name = tk.StringVar() # 6
nameEntered = ttk.Entry(win, width=12,textvariable=name) # 7
nameEntered.grid(column=0, row=1) # 8
nameEntered.focus()   #将鼠标光标定位在此中# Place cursor into name Entry
win.mainloop()