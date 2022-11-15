#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares 
# de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos 
# obtenidos mediante reduce.

from functools import reduce

def main():
    print("Ejercicio 2. Filter y Reduce")
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    impares = list(filter(lambda num:num%2!=0, numeros))
    suma = reduce(lambda a,b: a+b, impares)
    print(f"la suma de los numeros impares es: {suma}")

if __name__ == "__main__":
    main()