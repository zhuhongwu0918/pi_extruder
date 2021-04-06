from tkinter import ttk
import tkinter as tk
#https://www.cnblogs.com/yang-2018/p/11824250.html
#https://blog.csdn.net/weixin_42272768/article/details/100915973

win=tk.Tk()

tree=ttk.Treeview(win,height=10,show='headings',columns=('0','1','2'),selectmode = "extended")

tree.heading('0',text='one')
tree.column('0',width=150,anchor='center')
tree.heading('1',text='two')
tree.column('1',width=150,anchor='center')
tree.heading('2',text='three')
tree.column('2',width=150,anchor='center')

def print_pres(event):
    for i in tree.selection():
        print(tree.item(i,"values"))  
opp=ttk.Button(win,text='get')
opp.pack()
opp.bind('<Button-1>',print_pres)
tree.pack()
for i in range(10):
    tree.insert('','end',values=(0,i,i))#  ""表示父节点是根   end表示在数据下附加
ore=tree.get_children()
for i in ore:
    oree=tree.item(i,"values")
    print(oree)

win.mainloop()