# opcion 1
from operaciones import suma, resta
import pprint as p

def main():
    print ("starting app ...")
    num1 = 1
    num2 = 2

    # opcion 1
    print(num1, "+", num2, "=", suma.suma(num1, num2))
    print(num1, "-", num2, "=", resta.resta(num1, num2))

    p.pprint(dir(suma))

    help(suma.suma)
    

if __name__ == '__main__':
    main()