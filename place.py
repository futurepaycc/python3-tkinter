import tkinter
from tkinter import messagebox

top = tkinter.Tk()
top.geometry("400x300")

def helloClick():
    messagebox.showinfo("hello python","hello world")

b = tkinter.Button(top,text="Hello",command=helloClick)
b.place(x=0,y=0,width=50,height=50)

top.mainloop()