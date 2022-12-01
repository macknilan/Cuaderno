# abstract base classes

import abc, math


class Figura(abc.ABC):
    """
    Docstring Figura
    """

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimetro(self):
        pass


class Rectangulo(Figura):
    """
    Docstring Rectangulo
    """

    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    def area(sefl):
        return sefl._ancho * sefl._alto

    def perimetro(sefl):
        return 2 * (sefl._ancho * sefl._alto)


class Circulo(Figura):
    """
    Docstring Circulo
    """

    def __init__(self, radio):
        self._radio = radio

    def area(sefl):
        return math.pi * (sefl._radio**2)

    def perimetro(sefl):
        return 2 * math.pi * sefl._radio


# Recctangulo
rect = Rectangulo(10, 10)
print(f"El area de un rectangulo es -> {rect.area()}")
print(f"El perimetro de un rectangulo es -> {rect.perimetro()}")

# Circulo
circulo = Circulo(10)
print(f"El area de un circulo es -> {circulo.area()}")
print(f"El perimetro de un circulo es -> {circulo.perimetro()}")
