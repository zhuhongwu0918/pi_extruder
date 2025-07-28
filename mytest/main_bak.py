import tkinter as tk
from tkinter import ttk
import time as t
import threading as tr
import app_ui
import signal
import sys

win=tk.Tk()
win.title('test')

def func_button0():
    """
    Prints numbers from 0 to 8 with a 5-second delay between each print.
    Displays the message "What's your number:" followed by the current number.
    """
    for i in range(9):
        print('Waht\' your number:'+str(i))
        t.sleep(5)
def motor_control():
    """电机控制函数"""
    try:
        while True:
            print("Motor control running...")
            t.sleep(0.5)
    except KeyboardInterrupt:
        print("Motor control interrupted")
    pass
def manage_thread():
    runT=tr.Thread(target=func_button0, daemon=True)
    runT.start()
    runM=tr.Thread(target=motor_control, daemon=True)
    runM.start()
def exit_handler(signum, frame):
    print("\n正在退出程序...")
    sys.exit(0)
if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_handler)
    manage_thread()
    opp=app_ui.OOP()
    opp.createWidget()
    try:
        opp.mainloop()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        opp.destroy()
        sys.exit(0)
