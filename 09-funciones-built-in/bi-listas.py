
from functools import reduce

def main():
    print("FUNCIONES DE LISTAS")
    numeros = [1,2,3,4,5,6,7,8,9,10]

    # obtener los numeros pares de la lista
    pares = list(filter(lambda numero: numero%2==0, numeros))
    print(pares)

    # calcular el cuadrados de los numeros de la lista
    cuadrado = list(map(lambda numero: numero*numero, numeros))
    print(cuadrado)

    # calcular la sumatorias de los numeros de la lista
    suma = reduce(lambda a, b: a + b, numeros)
    print(suma)

    cursos = ["Python", "Java", "Go"]
    asistentes = [10, 15, 5]

    #zip genera una lista de tuplas con la combinancion de ambas listas
    result = zip(cursos, asistentes)
    print(list(result))

if __name__ == "__main__":
    main()