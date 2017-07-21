#coding:utf-8
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def butClick():
    messagebox.showinfo(title="按钮",message="你要干嘛")


btn1 = tk.Button(root,text="btn1",command=butClick).grid(row=0,column=0)
btn2 = tk.Button(root,text="btn2").grid(row=0,column=1)
btn3 = tk.Button(root,text="btn3").grid(row=1,column=0)
btn4 = tk.Button(root,text="btn4").grid(row=1,column=1)

root.mainloop()