import tkinter as tk # imports
from tkinter import ttk

win = tk.Tk() # Create instance 
win.title("Python GUI") # Add a title 
tabControl = ttk.Notebook(win) # Create Tab Control

tab1 = ttk.Frame(tabControl) # Create a tab 
tabControl.add(tab1, text='Tab 1') # Add the tab

# monty = ttk.LabelFrame(tab1, text=' Monty Python ')
# monty.grid(column=0, row=0, padx=8, pady=4)
# ttk.Label(monty, text="Enter a name:").grid(column=0, row=0,sticky='W')

tabControl.pack(expand=1, fill="both") # Pack to make visible https://www.cnblogs.com/zhangpengshou/p/3626137.html https://www.iteye.com/blog/purpen-74830

tab2 = ttk.Frame(tabControl) # Create a tab 
tabControl.add(tab2, text='Tab 2') # Add the tab

win.mainloop() # Start GUI