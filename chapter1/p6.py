# imports # 1
import tkinter as tk # 2
from tkinter import ttk # 3
win = tk.Tk() # 2 Create instance
win.title("Python GUI") # 3 Add a title 
#win.geometry('800x600+300+20') 
#win.resizable(0, 0) # 4 Disable resizing the GUI
# Adding a Label # 4
ttk.Label(win, text="A Label").grid(column=0, row=0) # 5
tk.Label(win,text="A Label1").grid(column=1, row=1)
win.mainloop() # 5 Start GUI