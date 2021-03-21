import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("my")
win.geometry('400x300')
# Radiobutton callback function # 4
def radCall1():
    radSel=radVar.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])
# First, we change our Radiobutton global variables into a list.
colors = ["Blue", "Gold", "Red"] # 1
# create three Radiobuttons using one variable
radVar = tk.IntVar()
#Next we are selecting a non-existing index value for radVar.
radVar.set(99) # 2
#Now we are creating all three Radiobutton widgets within one loop.
for col in range(3): # 3
    curRad = 'rad' + str(col) 
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall1)
    curRad.grid(column=col, row=6, sticky=tk.W)

win.mainloop()