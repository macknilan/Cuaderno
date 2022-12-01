import unittest


def suma(num_1, num_2):
    return num_1 + num_2


class CajaNegraTest(unittest.TestCase):
    """Las pruebas de caja negra se basan en la especificación de la función o el programa,

    aquí debemos probas sus inputs y validar los outputs. Se llama caja negra por que no
    necesitamos saber necesariamente los procesos internos del programa, solo contrastar sus resultados.
    Estos tipos de pruebas son muy importantes para 2 tipos de test:

    Unit testing: se realizan pruebas a cada uno de los módulos para determinar su correcto funcionamiento.

    Integration testing: es cuando vemos que todos los módulos funcionan entre sí.

    Es una buena práctica realizar los test antes de crear tus lineas de código,
    esto es por que cualquier cambio que se realice a futuro los test estarán
    incorporados para determinar si los cambios cumplen lo esperado.

    En Python existe la posibilidad de realizar test gracias a la librería unittest.
    Puede ser que el siguiente código no lo entiendas en su totalidad, pero en
    una próxima guía detallare mas el tema de clases en programación.

    https://docs.python.org/3.9/library/unittest.html
    """

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


if __name__ == "__main__":
    unittest.main()
