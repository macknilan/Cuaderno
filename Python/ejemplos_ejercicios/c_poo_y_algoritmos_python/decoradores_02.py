#  Decoradores

import time


def calcular_tiempo(function):
    def wrapper(*args, **kwargs):

        print(f"*args - {args} / **kwargs - {kwargs} 0")
        print(f"Antes de la ejecución")

        start = time.time()

        result = function(*args, **kwargs)

        print(f"Tiempo total: {time.time() - start} 1")

        return result

    return wrapper


@calcular_tiempo
def suma(a, b):
    time.sleep(2)
    return a + b


print(suma(2, 48))
