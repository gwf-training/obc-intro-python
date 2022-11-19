import tkinter as tk

#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción 
# que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada.

window = tk.Tk(className="Bienvenido")

def main():
    print("GUI - Ejercicio 1")
    lblCampeon = tk.Label(window, text="Quien va a salir campeon?")
    lblCampeon.pack()

    campeonSelected = tk.IntVar()

    def reiniciar():
        campeonSelected.set(value=-1)
        return

    rbARG = tk.Radiobutton(window, text="Argentina", variable=campeonSelected, value=1)
    rbARG.pack()

    rbBRA = tk.Radiobutton(window, text="Brasil", variable=campeonSelected, value=2)
    rbBRA.pack()

    rbESP = tk.Radiobutton(window, text="España", variable=campeonSelected, value=3)
    rbESP.pack()

    rbFRA = tk.Radiobutton(window, text="Francia", variable=campeonSelected, value=4)
    rbFRA.pack()

    reiniciarButton = tk.Button(window, text="Reiniciar", command=reiniciar)
    reiniciarButton.pack()

    tk.mainloop()
    return

if __name__ == "__main__":
    main()