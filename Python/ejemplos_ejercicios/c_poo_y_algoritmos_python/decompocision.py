class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo"
        self._motor = Motor(cilindros=4)

    def informacion_automovil(self):
        print(f"Informacion de -Automovil- motor:{self.modelo} marca: {self.marca} color:{self.color}")

    def acelerar(self, tipo="despacio"):
        if tipo == "rapida":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = "en_movimiento"
        print(f"El automovil va tipo: {tipo} y el estado es {self._estado}")


class Motor:
    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def informacion_motor(
        self, temperatura_motor
    ):  # Esta funcion es temporal, solo para revisar que todo esta funcionanndo
        self.temperatura_motor = temperatura_motor
        print(f"Informacion de -Motor- = tipo de combustion: {self.tipo} temperatura: {self.temperatura_motor}")

    def inyecta_gasolina(self, cantidad):
        self.cantidad = cantidad
        pass


if __name__ == "__main__":

    car1 = Automovil("ABC", "Nissan", "Plata")
    car1.informacion_automovil()
    car1._motor.informacion_motor(90)
    car1.acelerar()
