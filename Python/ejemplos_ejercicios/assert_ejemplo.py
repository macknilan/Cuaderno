def primera_palabra(lista_palabras):
    """
    assert <expresion booleana>, <mensaje de error>

    Es un mecanismo por el cuál podemos determinar si una función se
    cumple o no se cumple. Y poder seguir adelante con la ejecución
    de nuestro programa o terminar dicha ejecución.

    Programación defensiva: Pueden utilizarse para verificar que los
    tipos sean correctos en una función.

    También sirven para debuguear: Para generarlas tenemos que utilizar
    el keyword -assert- y dar una expresión booleana y un mensaje de error
    """
    primeras_letras = []

    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f"{palabra} no es string"
            assert len(palabra) > 0, "No se permiten espacios vacíos."
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras


lista = ["Nombre", 4.4, "", 2, "9483", 0.2344]

print("Primeras letras validas son: ", primera_palabra(lista))
