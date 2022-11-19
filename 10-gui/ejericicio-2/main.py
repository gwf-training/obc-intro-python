#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de 
# contener una lista de elementos seleccionables, también debe de tener un label 
# con el texto que queráis.

import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("GUI - ListBox")

labelPaises =tk.Label(window, text = "Paises")
listbox = tk.Listbox(window, height = 10, width = 15, bg = "grey", activestyle = 'dotbox', font = "Helvetica")
listbox.insert(1, "Argentina")
listbox.insert(2, "Bolivia")
listbox.insert(3, "Uruguay")
listbox.insert(4, "Chile")
listbox.insert(5, "Brasil")
listbox.insert(6, "Paraguay")
listbox.insert(7, "Colombia")
listbox.insert(8, "Venezuela")

labelPaises.pack()
listbox.pack()

tk.mainloop()