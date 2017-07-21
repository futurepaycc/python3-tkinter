import tkinter as tk

def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin,text="Do nothing button")
    button.pack()

root = tk.Tk()
root.geometry("400x300")
root.resizable(width=False,height=False)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=donothing)


menubar.add_cascade(label="file",menu=filemenu)

root.config(menu=menubar)
root.mainloop()