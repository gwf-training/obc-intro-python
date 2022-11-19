import tkinter
from tkinter import ttk

def main():
    window = tkinter.Tk(className="GEOMETRIA GRID")
    window.columnconfigure(0, weight=1)
    window.columnconfigure(0, weight=3)

    userNameLabel = ttk.Label(window, text="Username:")
    userNameLabel.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)
    userNameEntry = ttk.Entry(window)
    userNameEntry.grid(column=1, row=0, sticky=tkinter.W, padx=5, pady=5)

    passwordLabel = ttk.Label(window, text="Password:")
    passwordLabel.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)
    passwordEntry = ttk.Entry(window, show="*")
    passwordEntry.grid(column=1, row=1, sticky=tkinter.W, padx=5, pady=5)

    loginButton = ttk.Button(window, text="Login")
    loginButton.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)



    window.mainloop()
    print("finalizando app")

if __name__ == "__main__":
    main()