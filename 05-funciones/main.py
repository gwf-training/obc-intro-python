def mifuncion(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print("key: ", key, "value:", value)

def mifuncion2(**kwargs):
    if "color" in kwargs and kwargs["color"] == "rojo":
        print("El rojo es el mejor color")

def mifuncionConParametrosVariables(*args):
    suma = 0
    for numero in args :
        suma += numero
    print("suma:", suma)
    

def operaciones(a, b):
     return a+b, a-b, a*b, a/b

mifuncion(nombre="Willy", edad=40)
mifuncion2(color="rojo",  vehiculo="auto")
mifuncionConParametrosVariables(1,2,3,4)

resultadoOperaciones = operaciones(4, 8)
print("resultadoOperaciones: ", resultadoOperaciones)
print("operacion resta", resultadoOperaciones[1])

s, r, m, d = operaciones(3 , 5)
print("suma:", s)
print("resta:", r)
print("multiplicacion:", m)
print("division:", d)

