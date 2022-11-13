class Vehiculo:
    tipo = ""
    marca = ""
    modelo = ""
    color = ""

    def __init__(self, tipo, marca, modelo, color) -> None:
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def getTipo(self):
        return self.tipo

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getColor(self):
        return self.tipo
