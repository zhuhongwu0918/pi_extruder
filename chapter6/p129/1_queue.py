from threading import Thread
from time import sleep
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import queue
import os


win=tk.Tk()

que=queue.Queue()

def input_que():
    que.put("1")

button0=ttk.Button(win,text="hit me",command=input_que)
button0.pack()

scotext=scrolledtext.ScrolledText(win,width=40,height=6)
scotext.pack()

def read_queue():
    while True:
        scotext.insert(tk.INSERT,que.get())

Thread(target=read_queue).start()

def _destroyWindow():
    win.quit()
    win.destroy()
    os._exit(0) 

win.protocol('WM_DELETE_WINDOW', _destroyWindow)
win.mainloop()

que=queue.Queue()
que.put("2333")
que.put("111")
print(que.get())
print(que.get())