import calculadora as cal

def main ():
    print("iniciando ejercicio 1: Calculadora ...")

    print("Ingrese los valores de A y B para realizar las operaciones")
    numeroA = int(input("valor de A: "))
    numeroB = int(input("valor de B: "))

    # aplicar operaciones 
    print(numeroA, "+", numeroB, "=", cal.sumar(numeroA, numeroB))
    print(numeroA, "-", numeroB, "=", cal.restar(numeroA, numeroB))
    print(numeroA, "*", numeroB, "=", cal.multiplicar(numeroA, numeroB))
    print(numeroA, "/", numeroB, "=", cal.dividir(numeroA, numeroB))

if __name__ == "__main__":
    main()
