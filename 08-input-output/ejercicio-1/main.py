from os.path import exists
from datetime import datetime
import time

path = "C:\\Users\\gwfer\dev\\training\\open-bootcamp\\intro-python\\08-input-output\\ejercicio-1\\"

def main():
    print("iniciando ejercicio 1: files")

    fileName = "archivo.txt"
    fullPath = f"{path}{fileName}"
    file = None

    if not exists(fullPath):
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
