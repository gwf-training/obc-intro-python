import time
from datetime import datetime, timedelta

def main():
    print("Iniciando Alarma: Go home ...")
    horaAlarmaGoHome = 19
    horaActual = int(time.strftime("%H"))
    if horaActual >= horaAlarmaGoHome:
        print("Son las ", time.strftime("%H:%M:%S"),"Ya es hora de ir a casa!!")
    else:
        alarmaGoHome = datetime.strptime(time.strftime("%Y-%m-%d")+" "+str(horaAlarmaGoHome)+":00:00", "%Y-%m-%d %H:%M:%S")
        diff = alarmaGoHome - datetime.now()
        print("Vamos!!! solo faltan %s" % diff)

if __name__ == "__main__":
    main()