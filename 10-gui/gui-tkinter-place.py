import tkinter

def main():
    window = tkinter.Tk(className="GEOMETRIA PLACE")

    label1 = tkinter.Label(window, text="posicionamiento place", bg="blue", fg="white")
    label1.place(x=20, y=50)

    label2 = tkinter.Label(window, text="otro label mas", bg="red", fg="white")
    label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor="ne")

    window.mainloop()
    print("finalizando app")

if __name__ == "__main__":
    main()