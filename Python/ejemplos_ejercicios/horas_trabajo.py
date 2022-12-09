"""
Cuantas horas de trabajo en 20 días tomando lo minutos.
"""


def run(minutes: int) -> int:
    """
    Función para determinar las horas trabajadas en 20 días
    dados los minutos trabajados.
    :param minutes:
    :return: int
    """
    hrs = minutes / 60
    days = hrs / 20

    return int(days)


if __name__ == "__main__":

    while True:
        try:
            _minutes = int(input("Total de minutos:  "))
        except ValueError:
            print("Escribe correctamente los minutos")
            continue
        else:
            if isinstance(_minutes, int):
                print(f"{run(_minutes)} horas por día")
            break
