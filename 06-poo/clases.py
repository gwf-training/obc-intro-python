
class Dispositivo:
    def __init__(self) -> None:
        super().__init__()
        print("Estoy dentro del constuctor de Dispositivo")
        
    encendido = False
    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

class Tablet(Dispositivo):
    pulgadas = None

    def __init__(self, pulgadas) -> None:
        super().__init__()
        print("Estoy dentro del constuctor de", self.__class__)
        print(dir(self))
        self.pulgadas = pulgadas

tablet = Tablet(10)
print("pulgadas:",tablet.pulgadas)
tablet.encender()
print(tablet.encendido)
tablet.apagar()
print(tablet.encendido)




