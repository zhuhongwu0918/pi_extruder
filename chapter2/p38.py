import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext # 2
from tkinter import Menu

win = tk.Tk()
win.title("my")

monty = ttk.LabelFrame(win, text=' Python ')
monty.grid(column=0, row=0,padx=3,pady=3)

def clickMe(): # 2
    action.configure(text='Hello ' + name.get()+ ' ' +numberChosen.get())
    numberChosen.configure(state='disable')
    nameEntered.configure(state='disable')
action = ttk.Button(monty, text="Click Me!",command=clickMe)
# Modified Button Click Function # 1

# Position Button in second row, second column (zero-based)
action.grid(column=2, row=1)
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0) # 1
number = tk.StringVar() # 2
numberChosen = ttk.Combobox(monty, width=12, textvariable=number,value=(1, 2, 4, 42, 100)) #3#可以直接作为元组传入
#numberChosen['values'] = (1, 2, 4, 42, 100) # 4   #可以直接作为元组传入
numberChosen.configure(state='readonly') #限制用户选择，禁止选项内输入 对象生成时可用
numberChosen.grid(column=1, row=1) # 5
numberChosen.current(0) # 6

# Changing our Label # 3
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0) # 4
# Adding a Textbox Entry widget # 5
name = tk.StringVar() # 6
nameEntered = ttk.Entry(monty, width=12,textvariable=name) # 7
nameEntered.grid(column=0, row=1) # 8
nameEntered.focus()   #将鼠标光标定位在此中# Place cursor into name Entry

# Creating three checkbuttons # 1
chVarDis = tk.IntVar() # 2
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled') # 3
check1.select() # 4
check1.grid(column=0, row=4, sticky=tk.W) # 5 #west east tk.W左对齐，tk.E右对齐
chVarUn = tk.IntVar() # 6
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn)
check2.deselect() # 8
check2.grid(column=1, row=4, sticky=tk.W) # 9 
chVarEn = tk.IntVar() # 10
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
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
rad1 = tk.Radiobutton(monty, text=COLOR1, variable=radVar, value=1, command=radCall) # 9
rad1.grid(column=0, row=5, sticky=tk.W) # 10
rad2 = tk.Radiobutton(monty, text=COLOR2, variable=radVar, value=2, command=radCall) # 11
rad2.grid(column=1, row=5, sticky=tk.W) # 12
rad3 = tk.Radiobutton(monty, text=COLOR3, variable=radVar, value=3, command=radCall) # 13
rad3.grid(column=2, row=5, sticky=tk.W) # 14

# Add this import to the top of the Python Module # 1
#from tkinter import scrolledtext # 2
# Using a scrolled Text control # 3
scrolW = 30 # 4
scrolH = 4 # 5
#, wrap=tk.WORD
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD) # 6
scr.grid(column=0, columnspan=3,sticky=tk.EW,padx=20) # 7,sticky='WE'
# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ') # 1
labelsFrame.grid(column=1, row=7,padx=6,pady=6)

# Place labels into the container element # 2
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

for child in labelsFrame.winfo_children(): 
    child.grid_configure(padx=8, pady=4)    

menuBar = Menu(win) # 1------------开辟菜单并生成对象
win.config(menu=menuBar)#----------配置生效
#menuBar.add_command(label="233")

fileMenu = Menu(menuBar, tearoff=0) # 2----开辟生成按键菜单对象
fileMenu.add_command(label="New1")#配置按键菜单对象内容
#fileMenu.add_separator()
fileMenu.add_command(label="New2")
fileMenu.add_command(label="New3")#配置按键菜单对象内容

menuBar.add_separator()#设置间隔分隔
menuBar.add_cascade(label="File", menu=fileMenu)#将生成的按键菜单对象应用到菜单栏对象上
menuBar.add_separator()#设置间隔分隔

helpMenu = Menu(menuBar, tearoff=0) # 6
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)#将生成的按键菜单对象应用到菜单栏对象上

win.mainloop()