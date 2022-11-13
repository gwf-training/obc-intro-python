class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[nombre: {self.nombre}, precio: ${self.precio}]"


def main():
    edad = 44
    nombre = "Gustavo"
    completoCurso = True

    # opcion 1
    print("Nombre: %s, edad: %d, Completo el Curso: %s" % (nombre, edad, completoCurso))

    # opcion 2
    print("Nombre: {}, edad: {}, Completo el Curso: {}".format(nombre, edad, completoCurso))
    print("Nombre: {0}, edad: {1}, Completo el Curso: {2}".format(nombre, edad, completoCurso))
    print("Nombre: {n}, edad: {e}, Completo el Curso: {c}".format(n=nombre, e=edad, c=completoCurso))

    # opcion 2
    print(f"Nombre: {nombre}, edad: {edad}, Completo el Curso: {completoCurso}")

    potato = Juguete("potato", 10.5)
    print(potato)
    print(repr(potato))



if __name__ == "__main__":
    main()