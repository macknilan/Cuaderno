# polimorfismo

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f"Ando caminando {self.nombre}")


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f"Ando moviendome en mi bicicleta {self.nombre}")


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()