# complejidad algorítmica

import time


def factorial(n):
    respuesta = 1

    while n > 1:
        # print(f"respuesta: {respuesta} n: {n}")
        respuesta *= n
        # print(f"respuesta *= n -> {respuesta} n -> {n}")
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
