import tkinter as tk
from tkinter import ttk
from threading import Thread, Event
import queue
from motor_controller import MotorController
from proximity_sensor import ProximitySensor
import logging
from create_tool_tip import createToolTip
from tkinter import scrolledtext # 2
from tkinter import Menu
from tkinter import messagebox as mBox
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Extrusion control interface")
        self.geometry("500x600")
        self.protocol("WM_DELETE_WINDOW", self.safe_shutdown)
        
        # 创建停止事件和状态队列
        self.stop_event = Event()
        self.status_queue = queue.Queue()
        self.iconbitmap(r'.\favicon.ico')
        # 设置UI
        # self.setup_ui()
        self.createWidget()

        
        # 启动工作线程
        self.start_workers()
        # 启动UI更新循环
        self.after(100, self.update_ui)
    def clickMe(self): # 2
        self.action.configure(text='Hello ' + self.name.get()+ ' ' +self.numberChosen.get())
        self.numberChosen.configure(state='disable')
        self.nameEntered0.configure(state='disable')
        self.nameEntered1.configure(state='disable')
    def forward_motion(self): # 2
        self.action.configure(text='Hello ' + self.name.get()+ ' ' +self.numberChosen.get())
        print("forward_motion")
        # self.numberChosen.configure(state='disable')
        # self.nameEntered.configure(state='disable')
    def backward_motion(self): # 2
        self.action.configure(text='Hello ' + self.name.get()+ ' ' +self.numberChosen.get())
        print("backward_motion")
        # self.numberChosen.configure(state='disable')
        # self.nameEntered.configure(state='disable')       
    def backward_limit(self): # 2
        self.action.configure(text='Hello ' + self.name.get()+ ' ' +self.numberChosen.get())
        print("backward_limit_motion")
        # self.numberChosen.configure(state='disable')
        # self.nameEntered.configure(state='disable')    
    def forward_limit(self): # 2
        self.action.configure(text='Hello ' + self.name.get()+ ' ' +self.numberChosen.get())
        print("forward_limit_motion")
        # self.numberChosen.configure(state='disable')
        # self.nameEntered.configure(state='disable')    
    def createWidget(self):
        tabControl = ttk.Notebook(self) # Create Tab Control---------------
        self.tab1 = ttk.Frame(tabControl) # Create a tab 
        tabControl.add(self.tab1, text='Tab 1') # Add the tab--------------

        self.tab2 = ttk.Frame(tabControl) # Create a tab 
        tabControl.add(self.tab2, text='Tab 2') # Add the tab

        self.tab3 = ttk.Frame(tabControl) # Add a third tab
        tabControl.add(self.tab3, text='Tab 3') # Make second tab visible

        self.monty = ttk.LabelFrame(self.tab1, text=' 参数设置 ')
        self.monty.grid(column=0, row=3,padx=3,pady=3)

        self.monty1 = ttk.LabelFrame(self.tab2, text=' monty1 ')
        self.monty1.grid(column=0, row=0,padx=3,pady=3)

        # Tab Control 3 -------------------------------
        self.tab3 = tk.Frame(self.tab3, bg='blue')
        self.tab3.pack()
        for orangeColor in range(2):
            canvas = tk.Canvas(self.tab3, width=150, height=80, highlightthickness=0, bg='orange')
            canvas.grid(row=orangeColor, column=orangeColor)
        self.action = ttk.Button(self.monty, text="确认!",command=self.clickMe)
        # Modified Button Click Function # 1
        # Position Button in second row, second column (zero-based)
        self.action.grid(column=3, row=1)

        self.action = ttk.Button(self.monty, text="后退到底",command=self.backward_limit)
        # Modified Button Click Function # 1
        # Position Button in second row, second column (zero-based)
        self.action.grid(column=0, row=4)
        self.action = ttk.Button(self.monty, text="后退",command=self.backward_motion)
        # Modified Button Click Function # 1
        # Position Button in second row, second column (zero-based)
        self.action.grid(column=1, row=4)
        self.action = ttk.Button(self.monty, text="前进",command=self.forward_motion)
        # Modified Button Click Function # 1
        # Position Button in second row, second column (zero-based)
        self.action.grid(column=3, row=4)
        self.action = ttk.Button(self.monty, text="前进到头",command=self.forward_limit)
        # Modified Button Click Function # 1
        # Position Button in second row, second column (zero-based)
        self.action.grid(column=4, row=4)

        ttk.Label(self.monty, text="运动速度(cm/min):").grid(column=2, row=0) # 1
        number = tk.StringVar() # 2
        self.numberChosen = ttk.Combobox(self.monty, width=12, textvariable=number,value=(1, 2, 4, 42, 100)) #3#可以直接作为元组传入
        #numberChosen['values'] = (1, 2, 4, 42, 100) # 4   #可以直接作为元组传入
        self.numberChosen.configure(state='readonly') #限制用户选择，禁止选项内输入 对象生成时可用
        self.numberChosen.grid(column=2, row=1) # 5
        self.numberChosen.current(0) # 6


        # Changing our Label # 3
        ttk.Label(self.monty, text="针筒规格(mL):").grid(column=0, row=0) # 4
        # Adding a Textbox Entry widget # 5
        self.name = tk.StringVar() # 6
        self.nameEntered0 = ttk.Entry(self.monty, width=12,textvariable=self.name) # 7
        self.nameEntered0.grid(column=0, row=1) # 8
        self.nameEntered0.focus()   #将鼠标光标定位在此中# Place cursor into name Entry

        ttk.Label(self.monty, text="单次体积(mL)").grid(column=1, row=0) # 4
        # Adding a Textbox Entry widget # 5
        self.name = tk.StringVar() # 6
        self.nameEntered1 = ttk.Entry(self.monty, width=12,textvariable=self.name) # 7
        self.nameEntered1.grid(column=1, row=1) # 8
        self.nameEntered1.focus()   #将鼠标光标定位在此中# Place cursor into name Entry

        # Creating three checkbuttons # 1
        chVarDis = tk.IntVar() # 2
        check1 = tk.Checkbutton(self.monty1, text="Disabled", variable=chVarDis, state='disabled') # 3
        check1.select() # 4
        check1.grid(column=0, row=4, sticky=tk.W) # 5 #west east tk.W左对齐，tk.E右对齐
        chVarUn = tk.IntVar() # 6
        check2 = tk.Checkbutton(self.monty1, text="UnChecked", variable=chVarUn)
        check2.deselect() # 8
        check2.grid(column=1, row=4, sticky=tk.W) # 9 
        chVarEn = tk.IntVar() # 10
        check3 = tk.Checkbutton(self.monty1, text="Enabled", variable=chVarEn)
        check3.select() # 12
        check3.grid(column=2, row=4, sticky=tk.W) # 13

        # Radiobutton Globals # 1
        COLOR1 = "Blue" # 2
        COLOR2 = "Gold" # 3
        COLOR3 = "Red" # 4
        # Radiobutton Callback # 5
        def radCall(): # 6
            radSel=radVar.get()
            if radSel == 1: self.monty1.configure(text=COLOR1)
            elif radSel == 2: self.monty1.configure(text=COLOR2)
            elif radSel == 3: self.monty1.configure(text=COLOR3)
        # create three Radiobuttons # 7
        radVar = tk.IntVar() # 8
        #radVar1 = tk.IntVar() # 8
        rad1 = tk.Radiobutton(self.monty1, text=COLOR1, variable=radVar, value=1, command=radCall) # 9
        rad1.grid(column=0, row=5, sticky=tk.W) # 10
        rad2 = tk.Radiobutton(self.monty1, text=COLOR2, variable=radVar, value=2, command=radCall) # 11
        rad2.grid(column=1, row=5, sticky=tk.W) # 12
        rad3 = tk.Radiobutton(self.monty1, text=COLOR3, variable=radVar, value=3, command=radCall) # 13
        rad3.grid(column=2, row=5, sticky=tk.W) # 14

        def _spin():
            value = spin.get()
            print(value)
            scr.insert(tk.INSERT, value + '\n')
        # Adding a Spinbox widget
        spin =ttk.Spinbox(self.monty, from_=0, to=10,width=5,command=_spin)
        spin1 =ttk.Spinbox(self.monty, values=(1,3,5,7,8),width=5,command=_spin)
        spin.grid(column=0, row=5)
        spin1.grid(column=4, row=5)

        createToolTip(spin, 'This is a Spin control.')
        createToolTip(spin1, 'This is a Spin control1.')
        # Add this import to the top of the Python Module # 1
        #from tkinter import scrolledtext # 2
        # Using a scrolled Text control # 3
        scrolW = 30 # 4
        scrolH = 5 # 5
        #, wrap=tk.WORD
        scr = scrolledtext.ScrolledText(self.monty, width=scrolW, height=scrolH, wrap=tk.WORD) # 6
        scr.grid(column=0, columnspan=3,sticky=tk.EW,padx=20) # 7,sticky='WE'
        # scr.grid(column=0, columnspan=3,sticky=tk.EW,padx=20,pady=100,ipady=0)
        createToolTip(scr, 'This is a ScrolledText widget.')

        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.monty1, text=' Labels in a Frame ') # 1
        labelsFrame.grid(column=1, row=7,padx=6,pady=6)

        # Place labels into the container element # 2
        ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
        ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

        for child in labelsFrame.winfo_children(): 
            child.grid_configure(padx=8, pady=4)    

        menuBar = Menu(self) # 1------------开辟菜单并生成对象
        self.config(menu=menuBar)#----------配置生效
        #menuBar.add_command(label="233")
        def _quit():
            self.win.quit()
            self.win.destroy()
            exit()

        fileMenu = Menu(menuBar, tearoff=0) # 2----开辟生成按键菜单对象
        fileMenu.add_command(label="New1")#配置按键菜单对象内容
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",command=_quit)#配置按键菜单对象内容

        menuBar.add_separator()#设置间隔分隔
        menuBar.add_cascade(label="File", menu=fileMenu)#将生成的按键菜单对象应用到菜单栏对象上
        menuBar.add_separator()#设置间隔分隔

        def _msgBox():
            #mBox.showinfo('Python Message Info Box', 'A Python GUI created by 硬菜 using tkinter:\nThe year is 2021.') 
            # mBox.showwarning('Python Message Warning Box', 'A Python GUI created by 硬菜 using tkinter:\nWarning: There might be a bug in this code.')
            # mBox.showerror('Python Message Error Box', 'A Python GUI created by 硬菜 using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
            answer = mBox.askyesno("Python Message Dual Choice Box", "Are you sure you really wish to do this?")
            print(answer)
        # Add another Menu to the Menu Bar and an item
        # Display a Message Box
        # Callback function
        helpMenu = Menu(menuBar, tearoff=0) # 6
        helpMenu.add_command(label="About", command=_msgBox)
        menuBar.add_cascade(label="Help", menu=helpMenu)#将生成的按键菜单对象应用到菜单栏对象上

        tabControl.pack(expand=1, fill="both") # Pack to make visible



        self.status_frame = tk.LabelFrame(self, text="系统状态")
        self.status_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        # self.status_frame.pack(padx=10, pady=5, fill=tk.X, ipady=10)  # ipady=10 减少内部可用高度


        self.motor_label = tk.Label(
            self.status_frame, 
            text="电机状态: 等待启动...",
            anchor="w"
        )
        self.motor_label.pack(fill=tk.X, padx=5, pady=2)

        self.sensor_label = tk.Label(
            self.status_frame, 
            text="传感器状态: 等待启动...",
            anchor="w"
        )
        self.sensor_label.pack(fill=tk.X, padx=5, pady=2)
        # 日志区域
        self.log_text = tk.Text(self, height=2)
        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        self.log_text.insert(tk.END, "系统启动...\n")
        # 关闭按钮
        self.btn_stop = tk.Button(
            self, 
            text="安全关闭系统", 
            command=self.safe_shutdown,
            bg="#ff9999"
        )
        self.btn_stop.pack(pady=10)

    
    def start_workers(self):
        # 创建并启动线程
        self.motor_thread = MotorController(self.stop_event, self.status_queue)
        self.sensor_thread = ProximitySensor(self.stop_event, self.status_queue)
        
        self.motor_thread.start()
        self.sensor_thread.start()
    
    def update_ui(self):
        # 处理所有待更新的状态
        while not self.status_queue.empty():
            try:
                source, message = self.status_queue.get_nowait()
                if source == "motor":
                    self.motor_label.config(text=f"电机状态: {message}")
                elif source == "sensor":
                    self.sensor_label.config(text=f"传感器状态: {message}")
                
                # 添加到日志
                self.log_text.insert(tk.END, f"{message}\n")
                self.log_text.see(tk.END)
            except queue.Empty:
                break
        
        # 检查线程状态
        if not self.motor_thread.is_alive() and not self.sensor_thread.is_alive():
            self.log_text.insert(tk.END, "所有工作线程已安全退出\n")
            self.btn_stop.config(state=tk.DISABLED)
            return
        
        # 继续定期检查
        self.after(200, self.update_ui)
    
    def safe_shutdown(self):
        logging.info("接收到关闭信号")
        self.stop_event.set()  # 通知所有线程停止
        
        # 禁用关闭按钮防止重复点击
        self.btn_stop.config(state=tk.DISABLED, text="正在关闭...")
        self.log_text.insert(tk.END, "正在停止工作线程...\n")
        
        # 等待线程结束（非阻塞方式）
        self.after(100, self.check_threads)
    
    def check_threads(self):
        # 检查线程是否已停止
        if self.motor_thread.is_alive() or self.sensor_thread.is_alive():
            self.after(200, self.check_threads)
        else:
            self.log_text.insert(tk.END, "系统可以安全关闭\n")
            self.destroy()  # 关闭Tkinter窗口
    
    # def mainloop(self):
    #     self.mainloop()
