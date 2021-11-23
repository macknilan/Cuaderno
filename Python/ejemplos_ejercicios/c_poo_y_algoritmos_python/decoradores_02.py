#  Decoradores

import time


def calcular_tiempo(function):
    def wrapper(*args, **kwargs):
        print(f"*args - {args} / **kwargs - {kwargs}")
        print(f"Antes de la ejecucion")
        start = time.time()
        result = function(*args, **kwargs)

        print(f"Tiempo total: {time.time() - start}")

        return result

    return wrapper


@calcular_tiempo
def suma(a, b):
    time.sleep(2)
    return a + b


print(suma(3, 48))
