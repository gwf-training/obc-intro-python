def sumador(**kwargs):
    inicio = kwargs["inicio"] if "inicio" in kwargs else 0
    fin = kwargs["fin"] if "fin" in kwargs else inicio
    suma = 0
    for numero in range (inicio, fin):
        suma += numero
    return suma

print(sumador(inicio=2, fin=10))
print(sumador())