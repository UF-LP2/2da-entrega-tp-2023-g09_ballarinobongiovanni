import tkinter as tk
from tkinter import *
from src.clases import Hospital


hp=Hospital("hop")
ventana = Tk()

ventana.geometry('400x700')
ventana.configure(background="white")
ventana.title("Interfaz")
tk.Radiobutton(
    ventana,
    text = "Listar",
    font=("Courier",14),
    bg="blue",
    fg="white",
    command=lambda:hp.listar()
).pack()


"""label1=Label(ventana, text="Listar:")
label1.place(x=40, y=30)


bt1=Button(ventana, text="Listar", command=hp.listar())
bt1.place(x=60, y=80)"""

ventana.mainloop()