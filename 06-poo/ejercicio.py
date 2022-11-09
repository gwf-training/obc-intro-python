
#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color
#Ruedas
#Puertas
#
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad
#Cilindrada
#
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

from abc import ABC

class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def __str__(self) -> str:
        return "color: %s, ruedas: %i, puertas: %i" % (self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada) -> None:
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        return super().__str__() + ", velocidad: %i, cilindrada: %i" % (self.velocidad, self.cilindrada)

coche = Coche("Rojo", 4, 3, 180, 8)
print(coche)
