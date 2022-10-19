"""
Definir una función la cual nos permita conocer cuantos dígitos posee un número.

La función debe tener por nombre cantidad_digitos.
La función debe poseer el parámetro numero.
La función debe retornar la cantidad de dígitos del parámetro.
No es posible utilizar la función str.
"""


def cantidad_digitos(numero: int) -> int:
    longitud = len(str(numero))

    return longitud


if __name__ == "__main__":
    try:
        numero = int(input("Escribe un numero: "))
        digitos = cantidad_digitos(numero)
        print(digitos)
    except ValueError:
        print("Lo que escribiste no es un numero entero :-(")


# def cantidad_digitos(numero):
#     digitos = 0
#
#     while numero > 0:
#         numero = numero // 10
#         digitos +=1
#
#     return digitos