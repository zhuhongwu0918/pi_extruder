import tkinter as tk
from tkinter import ttk
import time as t
import threading as tr

win=tk.Tk()
win.title('test')

def func_button0():
    for i in range(9):
        print('Waht\' your number:'+str(i))
        t.sleep(5)
def run_func():
    runT=tr.Thread(target=func_button0)
    runT.start()        
button0=ttk.Button(win,text="button0",command=run_func)
button0.grid(column=0, row=5,stick='WNSE')


win.mainloop()