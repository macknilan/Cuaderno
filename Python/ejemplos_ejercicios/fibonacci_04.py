# for python 3.8.10
from functools import lru_cache


@lru_cache(maxsize=10000)
def fibonacci(n):
    """Si el valor se encuentra en cache se retorna."""
    if type(n) != int:
        raise TypeError("n debe de ser entero")
    if type(n) < 1:
        raise ValueError("n debe de ser positivo")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 51):
    print(f"{n} : {fibonacci(n)}")
