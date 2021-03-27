import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext # 2
win = tk.Tk()
win.title("my")
def clickMe(): # 2
    action.configure(text='Hello ' + name.get()+ ' ' +numberChosen.get())
    numberChosen.configure(state='disable')
    nameEntered.configure(state='disable')
action = ttk.Button(win, text="Click Me!",command=clickMe)
# Modified Button Click Function # 1

# Position Button in second row, second column (zero-based)
action.grid(column=2, row=1)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0) # 1
number = tk.StringVar() # 2
numberChosen = ttk.Combobox(win, width=12, textvariable=number,value=(1, 2, 4, 42, 100)) #3#可以直接作为元组传入
#numberChosen['values'] = (1, 2, 4, 42, 100) # 4   #可以直接作为元组传入
numberChosen.configure(state='readonly') #限制用户选择，禁止选项内输入 对象生成时可用
numberChosen.grid(column=1, row=1) # 5
numberChosen.current(0) # 6

# Changing our Label # 3
ttk.Label(win, text="Enter a name:").grid(column=0, row=0) # 4
# Adding a Textbox Entry widget # 5
name = tk.StringVar() # 6
nameEntered = ttk.Entry(win, width=12,textvariable=name) # 7
nameEntered.grid(column=0, row=1) # 8
nameEntered.focus()   #将鼠标光标定位在此中# Place cursor into name Entry

# Creating three checkbuttons # 1
chVarDis = tk.IntVar() # 2
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled') # 3
check1.select() # 4
check1.grid(column=0, row=4, sticky=tk.W) # 5 #west east tk.W左对齐，tk.E右对齐
chVarUn = tk.IntVar() # 6
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect() # 8
check2.grid(column=1, row=4, sticky=tk.W) # 9 
chVarEn = tk.IntVar() # 10
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select() # 12
check3.grid(column=2, row=4, sticky=tk.W) # 13

# Radiobutton Globals # 1
COLOR1 = "Blue" # 2
COLOR2 = "Gold" # 3
COLOR3 = "Red" # 4
# Radiobutton Callback # 5
def radCall(): # 6
 radSel=radVar.get()
 if radSel == 1: win.configure(background=COLOR1)
 elif radSel == 2: win.configure(background=COLOR2)
 elif radSel == 3: win.configure(background=COLOR3)
# create three Radiobuttons # 7
radVar = tk.IntVar() # 8
#radVar1 = tk.IntVar() # 8
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall) # 9
rad1.grid(column=0, row=5, sticky=tk.W) # 10
rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall) # 11
rad2.grid(column=1, row=5, sticky=tk.W) # 12
rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall) # 13
rad3.grid(column=2, row=5, sticky=tk.W) # 14

# Add this import to the top of the Python Module # 1
#from tkinter import scrolledtext # 2
# Using a scrolled Text control # 3
scrolW = 30 # 4
scrolH = 4 # 5
#, wrap=tk.WORD
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD) # 6
scr.grid(column=0, columnspan=3) # 7

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ') # 1
labelsFrame.grid(column=0, row=7,padx=20,pady=40)

# Place labels into the container element # 2
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

# Place cursor into name Entry
nameEntered.focus()

win.mainloop()