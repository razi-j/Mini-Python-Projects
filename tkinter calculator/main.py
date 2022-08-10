from tkinter import *

value = ""

def input_value(char):
    global value
    value = value+str(char)
    field.delete(1, END)
    field.delete(1, value)

def calculate():
    global value
    total = str(eval(value))
    field.delete(1, END)
    field.insert(1, total)

def clear():
    global value
    value = ""
    field.delete(1,END)

root = Tk()
root.geometry("320x324")
root.title("Calculator")
root.resizable(0,0)
field = Text(root, height=2, width=21, font=("Times New Roman", 21))

field.pack()
root.mainloop()

