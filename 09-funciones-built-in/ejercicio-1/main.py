def main():
    print("EJERICIO 1")
    #argentina,brasil,CHILE,Bolivia, URuguaY,Argentina
    paisesInput = input("ingrese una lista de paises (separados por coma): ")
    paises = set(map(lambda p: str(p).lower().strip(), paisesInput.split(",")))
    paisesSorted = sorted(paises)
    print(",".join(paisesSorted))



if __name__ == "__main__":
    main()