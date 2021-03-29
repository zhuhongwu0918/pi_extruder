import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import socket as sk
import threading as tr

class sk_connect():
    def __init__(self,data):
        self.cli=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        self.cli.connect(data)
    def send(self,data):
        self.cli.send(bytes(data.encode()))
    def recv(self):
        return self.cli.recv(255)

start_sk=sk_connect(('127.0.0.1',24000))

def button0_send():
    start_sk.send("hit")

win=tk.Tk()

button0=ttk.Button(win,text="button0",command=button0_send)
button0.pack()

socText=scrolledtext.ScrolledText(win,width=40,height=5)
socText.pack()

def show_recv():
    while True:
        socText.insert(tk.INSERT,start_sk.recv())
runT=tr.Thread(target=show_recv)
runT.start()
win.mainloop()