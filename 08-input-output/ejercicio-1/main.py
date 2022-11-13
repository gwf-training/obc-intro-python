from os import path
from datetime import datetime
import time


def main():
    print("iniciando ejercicio 1: files")
    directoryPath = path.dirname(path.realpath(__file__))

    fileName = "archivo.txt"
    fullPath = f"{directoryPath}\\{fileName}"
    file = None

    if not path.exists(fullPath):
        file = open(fullPath, "x")
        print(f"archivo {fileName} creado")
        file.close()
    else:
        print(f"El archivo {fileName} ya existe")

    file = open(fullPath, "a")
    t = time.strftime("%d/%m/%y %H:%M:%S")
    file.write(f"[{t}]: Esta es una nueva linea agrega al archivo \n")
    file.close()

if __name__ == "__main__":
    main()
