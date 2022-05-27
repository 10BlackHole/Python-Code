from tkinter import *
from tkinter import messagebox

def accion():
    messagebox.showinfo("Aviso", "Datos enviados")

root = Tk()
root.config(bd=15)

usuario = Label(root, text="Usuario")
usuario.grid(row=1, column=0)

entry2 = Entry(root)
entry2.grid(row=1, column=1)

contraseña = Label(root, text="Contraseña")
contraseña.grid(row=2, column=1)

entry3 = Entry(root)
entry3.grid(row=2, column=1)
entry3.config(show="*")

boton = Button(root, text="Clícame", command=accion)
boton.grid(row=2, column=1)

root.mainloop()
