def sumar (a: int, b: int) -> int:
    ''' Esta función calcula y retorna la suma de 2 numeros enteros.
    @param a: int
    @param b: int
    '''
    assert type(a) is int, "el parametro 'a' debe ser un entero :("    
    assert type(b) is int, "el parametro 'b' debe ser un entero :("    
    return a + b

def restar (a: int, b: int) -> int:
    ''' Esta función calcula y retorna la resta de 2 numeros enteros.
    @param a: int
    @param b: int
    '''
    assert type(a) is int, "el parametro 'a' debe ser un entero :("    
    assert type(b) is int, "el parametro 'b' debe ser un entero :("    
    return a - b

def multiplicar (a: int, b: int) -> int:
    ''' Esta función calcula y retorna la multiplicacion de 2 numeros enteros.
    @param a: int
    @param b: int
    '''
    assert type(a) is int, "el parametro 'a' debe ser un entero :("    
    assert type(b) is int, "el parametro 'b' debe ser un entero :("    
    return a * b

def dividir (a: int, b: int) -> float:
    ''' Esta función calcula y retorna la division de 2 numeros enteros. 
    @param a: int
    @param b: int
    '''
    assert type(a) is int, "el parametro 'a' debe ser un entero :("    
    assert type(b) is int, "el parametro 'b' debe ser un entero :("
    return a / b

def moduleName() -> str:
    return __name__