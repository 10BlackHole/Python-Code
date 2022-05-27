import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Primera ventana")
ventana.geometry("300x300")
# ventana.configure(background='dark turquoise')
ventana.configure(background='yellow')

etiqueta1 = tk.Label(ventana, text="Hola Mundo!", bg="red", fg="white")
etiqueta1.pack()
# entry = ttk.Entry() # show="*" for passwords

ventana.mainloop()
