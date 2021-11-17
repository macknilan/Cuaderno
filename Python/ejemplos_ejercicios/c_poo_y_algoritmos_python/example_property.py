class Millas:
    def __init__(self):
        self._distancia = 0

    # Función para obtener el valor de _distancia
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Función para definir el valor de _distancia
    def definir_distancia(self, recorrido):
        print("Llamada al método setter")
        self._distancia = recorrido

    # Función para eliminar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia

    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


if __name__ == "__main__":

    # Creamos un nuevo objeto
    avion = Millas()

    # Indicamos la distancia
    avion.distancia = 200

    # Obtenemos su atributo distancia
    print(avion.distancia)
    # Llamada al método getter
    # Llamada al método setter
    # 200
