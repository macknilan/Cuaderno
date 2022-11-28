"""
Programa para determinar si un RFC es de persona moral o física.
"""


class rfc(object):
    """Constructor"""

    def __init__(self, rfc):
        self._rfc = rfc

    def valida_rfc(self) -> str:
        """Funcion para validar el rfc"""

        if len(self._rfc) == 13:
            fisica = "RFC de persona física."

        elif len(self._rfc) == 12:
            fisica = "RFC de persona moral."

        return fisica


if __name__ == "__main__":
    _rfc = str(input("Escribe el RFC que se desea verificar:  "))

    if len(_rfc) == 0 or 13 >= len(_rfc) <= 11 or len(_rfc) >= 14:
        print("Error al obtener el RFC.")
    else:
        tipo = rfc(_rfc)
        print(tipo.valida_rfc())
