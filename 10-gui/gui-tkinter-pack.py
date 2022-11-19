import tkinter

def main():
    window = tkinter.Tk(className="Bienvenido")

    labelSaludo = tkinter.Label(window, text="Bienvenido", bg="blue", foreground="white")
    labelSaludo.pack(ipadx="50", ipady="100")

    labelAdios = tkinter.Label(window, text="Adios", bg="red", fg="white")
    labelAdios.pack(ipadx="64", ipady="100", fill="both")

    window.mainloop()
    print("finalizando app")

if __name__ == "__main__":
    main()