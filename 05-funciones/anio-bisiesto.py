def isBisiesto(anio):
    return (anio%4==0 and anio%100!=0) or anio%400==0

aaaa = 2012
if isBisiesto(aaaa): 
    print("El año ", aaaa, "ES bisiesto")
else:
    print("El año ", aaaa, "NO es bisiesto")
