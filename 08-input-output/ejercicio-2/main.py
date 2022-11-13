import os
import pickle
import model

def main():
    print("iniciando ejercicio 2. files")
    directoryPath = os.path.dirname(os.path.realpath(__file__))

    tcross = model.Vehiculo("Auto", "Volkswagen", "T-cross", "Rojo")

    #serealizar objeto tcross en un archivo
    file = open(directoryPath+"\\tcrooss.bin", "wb")
    pickle.dump(tcross, file)
    file.close()

    #deserearilizar objeto tcross desde un archivo
    file = open(directoryPath+"\\tcrooss.bin", "rb")
    tcrossFromFile = pickle.load(file)
    file.close()

    print(tcrossFromFile.getModelo())



if __name__ == "__main__":
    main()