def suma (a: int, b: int) -> int:
    ''' Esta función calcula y retorna la suma de 2 numeros enteros.
    @param a: int
    @param b: int
    '''
    assert type(a) is int, "el parametro 'a' debe ser un entero :("    
    assert type(b) is int, "el parametro 'b' debe ser un entero :("    
    return a + b

def moduleName() -> str:
    return __name__
