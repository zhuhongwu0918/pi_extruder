# strVar = StringVar() # Holds a string; the default value is an empty string ""
# intVar = IntVar()# Holds an integer; the default value is 0
# dbVar = DoubleVar()# Holds a float; the default value is 0.0
# blVar = BooleanVar()# Holds a Boolean, it returns 0 for false and 1 for true
import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()
#set strData variable
strData.set('hello Stringvar')
#get value of strdata variable
varData = strData.get()

print(varData)