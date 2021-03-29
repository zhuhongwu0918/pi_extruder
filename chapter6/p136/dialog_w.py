from tkinter import filedialog
from os import path
import tkinter as tk

win=tk.Tk()  #shutil https://www.cnblogs.com/iamjianghao/p/11899792.html
def getFileName():
    fDir=path.dirname(__file__)
    print(fDir)
    fName=filedialog.askopenfilename(parent=win,initialdir=fDir)
    print(fName)
getFileName()
win.mainloop()

