
mensaje = "Hola Mundo!!!!"
print(mensaje)


c1 = {1,3,5,7}
c2 = {1,2,7,9,4}
c3 = c1 | c2 #union
c4 = c1 & c2 #interseccion
print("union: ", c3)
print("interseccion: ", c4)

a = 6
if a == 5:
    print("dentro del if")
    print("sigo")
else:
    print("else")
