import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

btn1 = tk.Button(root,text="btn1")
btn1.pack(fill=tk.X)

btn2 = tk.Button(root,text="btn2")
btn2.pack(side=tk.LEFT,fill=tk.Y)

root.mainloop()