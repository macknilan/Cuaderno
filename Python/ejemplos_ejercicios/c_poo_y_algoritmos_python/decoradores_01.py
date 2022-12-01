#  Decoradores


def my_custom_decorator(function):  # function_b = saludar/suma
    def wrapper(*args, **kwargs):
        print(f"*args - {args} / **kwargs - {kwargs} 0")
        print(f"Antes de la ejection")

        resultado = function(*args, **kwargs)

        print(f"Después de la ejection")
        print(f"*args - {args} / **kwargs - {kwargs} 1")

        return resultado

    return wrapper


@my_custom_decorator
def saludar():
    print(f"Hola desde la función -saludar-")


@my_custom_decorator
def suma(a, b):
    return a + b


suma(4, 3)
# saludar()
