def main():
    print("BUILT-IN VARIAS")

    # funciones all y any
    lista = [ 1 == 1, 2 == 2, 3 == 4]
    print("any: ", any(lista))
    print("all: ", all(lista))

    #funcion round
    print(round(5, 2))
    print(round(5.114, 2))
    print(round(5.115, 2))
    print(round(5.116, 2))


if __name__ == "__main__":
    main()