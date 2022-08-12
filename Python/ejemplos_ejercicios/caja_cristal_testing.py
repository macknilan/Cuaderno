import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    """Pruebas de caja de cristal

    Se basan en el flujo del programa, por lo que se asume que conocemos el
    funcionamiento del programa, por lo que podemos probar todos los caminos
    posibles de una función. Esto significa que vamos a probar las
    ramificaciones, bucles for y while, recursiones, etc.

    Este tipo de pruebas son muy buenas cuando debemos realizar:
    Regression testing o mocks:
    descubrimos un bug cuando corremos el programa, por lo que vamos a
    buscar el bug gracias a que conocemos como esta estructurado el código.
    """

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # unittest.main()
