# EJEPLO DE FUNCIONES DE ORDEN SUPERIOR

def cuadrado(x):
    """
    FUNCIÓN QUE DEVUELVE EL CUADRADO DE UN NÚMERO
    """
    return x * x


numeros = [1, 2, 3, 4, 5]
resultados = map(cuadrado, numeros)  # DEVUELVE UN OBJETO MAP

print(list(resultados))  # [1, 4, 9, 16, 25]