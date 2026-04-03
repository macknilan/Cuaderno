# EJEMPLO DE FUNCIONES DE ORDEN SUPERIOR

def multiplicar_por(n):
    """
    Crea una función de cierre que multiplica su entrada por un factor especificado.

    Argumentos:
        n (int): El factor por el cual multiplicar.

    Devuelve:
        function: Una función que toma un entero x y devuelve x multiplicado por n.
    """
    def multiplicar(x):
        """
        Multiplica un número dado por el factor de la función externa.

        Argumentos:
            x (int): El número a multiplicar.

        Devuelve:
            int: El resultado de multiplicar x por el factor de la función externa.
        """
        return x * n
    return multiplicar


# Uso del ejemplo
doblar = multiplicar_por(2)  # Crea una función que duplica la entrada
print(doblar(5))  # Salida: 10
