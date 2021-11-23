#  Decoradores


def my_custom_decorator(function):  # funcion_b = saludar/suma
    def wrapper(*args, **kwargs):
        print(f"*args - {args} / **kwargs - {kwargs}")
        print(f"Antes de la ejecucion")
        resultado = function(*args, **kwargs)
        print(f"Despues de la ejecucion")
        print(f"*args - {args} / **kwargs - {kwargs}")

        return resultado

    return wrapper


@my_custom_decorator
def saludar():
    print(f"Holas desde la cuncion a")


@my_custom_decorator
def suma(a, b):
    return a + b


print(suma(4, 3))
