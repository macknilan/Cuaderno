class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        print(region)
        if region in self._pais:
            self._region = region
            raise ValueError(
                f"La region {region} no es valida o ya se encuentra en {self._pais}"
            )


# casilla = CasillaDeVotacion(123, ["CDMX", "Morelos"])
#  print(casilla.region)
# None
#
#
# casilla.region = "CDMX"
# ValueError: La region CDMX no es valida o ya se encuentra en ['CDMX', 'Morelos']
#
# casilla.region = "CDMX."
# print(casilla.region)
# "CDMX."
