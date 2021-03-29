from urllib.request import urlopen
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def get_html():
    link = 'http://www.baidu.com' 
    try:
        f = urlopen(link)
        print(f)
        html = f.read()
        # print(html)
        htmldecoded = html.decode()
        scotext.insert(tk.INSERT,htmldecoded) 
    except Exception as ex:
        print('*** Failed to get Html! ***\n\n' + str(ex))

win=tk.Tk()

button0=ttk.Button(win,text='get',command=get_html)
button0.pack()

scotext=scrolledtext.ScrolledText(win,width=90,height=5)
scotext.pack()


win.mainloop()
