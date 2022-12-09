"""
Ejemplo de @classmethod
Contar  cuantas veces se crea un objeto
de la clase Accumulator
"""


class Accumulator:
    count = 0  # Atributo de la clase

    def __init__(self):
        Accumulator.increase_count()
        print(f"EL TRIBUTO  DE LA CLASE self.count -> {self.count}")
        self.acc = 0
        print(f"SE INICIALIZA LA CLASE CON TRIBUTO self.acc -> {self.acc}")

    def add(self, x):
        self.acc += x

    @classmethod
    def increase_count(cls):
        print("SE INCREMENTA A UNO EL ATRIBUTO DE LA CLASE count")
        cls.count += 1

    @classmethod
    def get_count(cls):
        print("RETORNA EL VALOR count")
        return cls.count


if __name__ == "__main__":
    a = Accumulator()
    # se crea un objeto de la clase del accumulator
    print(Accumulator.get_count())

    b = Accumulator()
    # se crea otro objeto de la clase accumulator
    print(Accumulator.get_count())

    c = Accumulator()
    # se crea otro objeto de la clase accumulator
    print(Accumulator.get_count())
