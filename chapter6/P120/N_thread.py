import tkinter as tk
from tkinter import ttk
import time as t

win=tk.Tk()
win.title('test')

def func_button0():
    for i in range(9):
        print('Waht\' your '+str(i))
        t.sleep(5)
button0=ttk.Button(win,text="button0",command=func_button0)
button0.grid(column=0, row=5,stick='WNSE')

win.mainloop()