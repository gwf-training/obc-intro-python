#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno 
# que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos 
# y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota

    def __str__(self) -> str:
        return "nombre: %s, nota: %i" % (self.nombre, self.nota)

    def evaluar(self) -> None:
        if self.nota >= 7:
            print("Nota: %i - APROBADO" % self.nota)
        else:
            print("Nota: %i - DESAPROBADO" %  self.nota)

juan = Alumno("Juan", 9)
print("Alumno: ", juan.nombre)
juan.evaluar()

pedro = Alumno("Pedro", 6)
print("Alumno: ", pedro.nombre)
pedro.evaluar()