"""
Ejemplo de una función que actua como decorador
"""


def funcion_decoradora(funcion_pararametro):
    """Función que actua como decorador"""

    def funcion_anterior():
        # ACCIONES ADICIONALES QUE DECORAN
        print("Se va a realizar un calculo")
        funcion_pararametro()

        # ACCIONES ADICIONALES QUE DECORAN
        print("Se termina el calculo")

    return funcion_anterior


@funcion_decoradora
def suma():
    print(15 + 15)


@funcion_decoradora
def resta():
    print(30 - 10)


suma()

resta()
