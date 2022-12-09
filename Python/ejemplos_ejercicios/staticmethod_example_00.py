"""
Ejemplo funcionamiento de @staticmethid
"""


class Accumulator:
    def __init__(self):
        self.acc = 0
        print(f"INICIALIZA LA FUNCIÓN Accumulator CON self.acc -> {self.acc}")

    def add(self, x):
        print(f"VALOR ANTES DE self.acc -> {self.acc}")
        print(f"SE LLAMA A AL FUNCIÓN add CON EL PARÁMETRO x -> {x}")
        self.acc += x
        print(f"VALOR DESPUÉS DE self.acc -> {self.acc}")

    @staticmethod
    def sub(x, y):
        return x - y


if __name__ == "__main__":
    a = Accumulator()
    a.add(23)
    a.add(42)

    print(f" VALOR TOTAL DE LA FUNCIÓN add CON EL VALOR DE acc -> {a.acc}")
    print(f"LLAMADA A LA FUNCIÓN staticmethod -> {Accumulator.sub(23, 42)}")
    print(f"LLAMADA A LA FUNCIÓN staticmethod -> {a.sub(20, 3)}")
