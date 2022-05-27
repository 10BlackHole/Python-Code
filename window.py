from tkinter import  *

root = Tk()
root.geometry("300x300")
var = StringVar()
label = Message(root, textvariable=var, relief=RAISED)

var.set = ("Hola")
label.pack()
root.mainloop()
