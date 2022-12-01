#  Decoradores

import time


def calcular_tiempo(name):
    def wrapper(function):
        def wrapper_2(*args, **kwargs):

            print(f"*args - {args} / **kwargs - {kwargs}")
            print(f"Antes de la ejecución")

            start = time.time()

            result = function(*args, **kwargs)

            print(f"Tiempo de tiempo de la función {name} total: {time.time() - start}")

            return result

        return wrapper_2

    return wrapper


@calcular_tiempo("suma")
def suma(a, b):
    time.sleep(2)
    return a + b


print(suma(3, 48))
