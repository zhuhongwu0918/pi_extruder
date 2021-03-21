#We are preventing the GUI from being resized.
import tkinter as tk # 1 imports
win = tk.Tk() # 2 Create instance
win.title("Python GUI") # 3 Add a title 
win.resizable(0, 0) # 4 Disable resizing the GUI 对应横轴和纵轴，0，1使能调整大小；
win.mainloop() # 5 Start GUI