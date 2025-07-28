from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
#--------------------------------------------------------------
fig = Figure(figsize=(12, 5), facecolor='white')
#--------------------------------------------------------------
axis = fig.add_subplot(111) # 1 row, 1 column
xValues = [1,2,3,4]
yValues0 = [6,7.5,8,7.5]
yValues1 = [5.5,6.5,2,9.6]
yValues2 = [6.5,7,8,7]
t0, = axis.plot(xValues, yValues0,color='purple')
t1, = axis.plot(xValues, yValues1,color='red')
t2, = axis.plot(xValues, yValues2,color='blue')   #变量加逗号可以把长度为1的元组中的元素提取出来https://www.cnblogs.com/azureology/p/12343730.html
#dynamical set scale------------------------------------------------
minx=min(xValues)
maxx=max(xValues)
axis.set_xlim(minx,maxx)
y_all=yValues0+yValues1+yValues2
print(y_all)
miny=min(y_all)
maxy=max(y_all)

axis.set_ylim(miny,maxy) #限制显示范围
#dynamical set scale-------------------------------------------------
axis.set_ylabel('Vertical Label')
axis.set_xlabel('Horizontal Label')
axis.grid()
 
fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')

#--------------------------------------------------------------
def _destroyWindow():
    root.quit()
    root.destroy()
#--------------------------------------------------------------
root = tk.Tk() 
label=tk.Label(root,text='233')
label.pack()
frame=tk.Frame(root, bg='blue')
frame.pack()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow) #root gui界面退出处理
#--------------------------------------------------------------
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#--------------------------------------------------------------
root.update()
root.deiconify()
root.mainloop()